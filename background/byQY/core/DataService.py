#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/28 18:14
# @Author  : yq
# @Site    : 
# @File    : DataService.py
# @Software: PyCharm
# 连接FTP
import datetime
import os
from background.byQY.core.BaseDao import BaseDao
from background.byQY.core.FTPManager import FTPManager
from background.byQY.model.DataModel import DataArea, DataDataInfo, DataCategory, DataSource


class DataService:
    def __init__(self, config_path, section_neargoos, section_mysql):
        self.ftp_Manager = FTPManager(config_path, section_neargoos)
        self.username = ""
        self.password = ""
        self.config_path = config_path
        self.section_neargoos = section_neargoos
        self.section_mysql = section_mysql
        self.dao = BaseDao(config_path, section_mysql)

    @staticmethod
    def switch_category(value):
        """
        根据后缀解析数据类型
        :param value: 后缀名
        :return: 数据类型
        """
        switcher = {
            "xml": "FUB",
            "bbx": "SHIP"
        }
        return switcher.get(value, 'STATION')

    def get_file_info(self):
        """
        获取数据信息列表
        :return file_infos: 数据信息列表
        """

        # 获取配置文件信息
        config = self.ftp_Manager.get_config()
        host = config.get(section_neargoos, 'host')
        self.username = config.get(section_neargoos, 'username')
        self.password = config.get(section_neargoos, 'password')
        target = config.get(section_neargoos, 'target')
        self.ftp_Manager.ftp_connect(host, self.username, self.password)
        file_infos = self.ftp_Manager.get_filename("", target)

        return file_infos

    def save_files(self, file_infos):
        """
        转存文件到指定目录，且将文件信息存入数据库的DataInfo表中
        [to-do]] 后续可将重复代码优化
        :param file_infos: 数据信息列表
        :return:
        """
        # 1. 创建数据库连接

        # 2.遍历文件名称列表
        print(file_infos)
        i = 0
        for file_info in file_infos:
            # 2.1. 解析目录名
            extension = file_info[-3:]
            # 2.2 一级目录文件名（数据类型）
            folder_level1 = DataService.switch_category(extension)
            i = i + 1
            print(i)

            if folder_level1 == 'FUB':
                # 2.2 三级目录文件名（年）
                folder_level2 = file_info[0:4]
                # 2.3 四级目录文件名（月）
                folder_level3 = file_info[4:6]
                # 2.4 五级目录文件名（日）
                folder_level4 = file_info[6:8]
                # [to-do] 暂时只有一个浮标，以后增加时需要修改
                extension = 'QD'
            elif folder_level1 == 'STATION':
                folder_level2 = str(datetime.datetime.now().year)
                folder_level3 = file_info[0:2]
                folder_level4 = file_info[2:4]
                time = file_info[4:6]
                # UTC时间和系统时间调整
                if folder_level3 == '12' and folder_level4 == '31' and time > 16:
                    folder_level2 = str(int(folder_level2) + 1)

            elif folder_level1 == 'SHIP':
                folder_level2 = str(datetime.datetime.now().year)
                folder_level3 = file_info[2:4]
                folder_level4 = file_info[4:6]
                hour = file_info[6:8]
                # [to-do] 暂时只有一个志愿船，以后增加时需要修改
                extension = 'default'
                # UTC时间和系统时间调整
                if folder_level3 == '12' and folder_level4 == '31' and int(hour) > 16:
                    folder_level2 = str(int(folder_level2) + 1)

            # 3.先将文件下载到本地
            # [to-do] Linux下需修改
            local_path_dir = os.path.join('E:', r'\temp', folder_level1, extension, folder_level2, folder_level3,
                                          folder_level4, "")
            remote_path_dir = '/'
            is_success = self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info,
                                                        local_path_dir)
            if is_success:
                print('下载数据成功')
                date_str = folder_level2 + '-' + folder_level3 + '-' + folder_level4
                url = os.path.join(folder_level1, extension, folder_level2, folder_level3,
                                   folder_level4, "")
                # 4.封装实体
                self.insert_data_info(file_info, folder_level1, extension, date_str, url)
        self.ftp_Manager.close_connect()

    def insert_data_info(self, file_info, folder_level1, extension, date_str, url):
        """
        封装实体
        :param file_info:
        :param extension:
        :param date_str:
        :param location:
        :param url:
        :return:
        """
        # 4.1 [to-do]得到对应的海区ID（暂时均为默认海区）
        area_result = self.dao.find_by_name(DataArea, 'default')
        # 4.2 [to-do]得到数据源的ID（暂时均为中国）
        source_result = self.dao.find_by_name(DataSource, 'China')
        # 4.3 [to-do]得到数据类型的ID（暂时均为中国）
        category_result = self.dao.find_by_name(DataCategory, folder_level1)
        datainfoModel = DataDataInfo()
        info = DataDataInfo()
        info.gmt_create = datetime.datetime.now()
        info.gmt_modified = datetime.datetime.now()
        info.name = file_info
        info.extensions = extension
        # [to-do]暂时没有备注
        info.date = datetime.datetime.strptime(date_str, '%Y-%m-%d').time()
        info.area_id = area_result.id
        info.category_id = category_result.id
        info.source_id = source_result.id
        info.url = url
        # [to-do]暂时没有FTP文件的最新修改日期
        info.size = self.ftp_Manager.size(file_info)
        info.location = extension
        self.dao.insert_one(info)

config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\Config.ini'
section_neargoos = 'neargoos'
section_mysql = 'mysql'
data_service = DataService(config_path, section_neargoos, section_mysql)
fileinfo = data_service.get_file_info()
data_service.save_files(fileinfo)

