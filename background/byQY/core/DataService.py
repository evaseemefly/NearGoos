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

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from background.byQY.core.FTPManager import FTPManager
from background.byQY.core.TimeUtil import TimeUtil
from background.byQY.model.DataFileInfo import DataFileInfo
# import pymysql
from background.byQY.model.DataModel import DataArea, DataDataInfo, DataCategory


class DataService:
    def __init__(self, config_path, section):
        self.ftp_Manager = FTPManager(config_path, section)
        self.username = ""
        self.password = ""

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
        host = config.get(section, 'host')
        self.username = config.get(section, 'username')
        self.password = config.get(section, 'password')
        target = config.get(section, 'target')
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
        engine = create_engine("mysql+pymysql://" + self.username + ":" + self.password + "@localhost:3306/neargoos",
                               max_overflow=5, echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        print(file_infos)
        i = 0
        for file_info in file_infos:
            # 1. 解析目录名
            extension = file_info[-3:]
            # 一级目录文件名
            folder_level1 = DataService.switch_category(extension)
            i = i + 1
            print(i)
            # 二级目录文件名
            if folder_level1 == 'FUB':
                folder_level2 = file_info[0:4]
                folder_level3 = file_info[4:6]
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

            # 2.先将文件下载到本地
            # [to-do] Linux下需修改
            local_path_dir = os.path.join('E:', r'\temp', folder_level1, extension, folder_level2, folder_level3,
                                          folder_level4, "")
            remote_path_dir = '/'
            is_success = self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info,
                                                        local_path_dir)
            if is_success:
                print('下载台站数据成功')
                location = extension
                date_str = folder_level2 + '-' + folder_level3 + '-' + folder_level4
                url = os.path.join(folder_level1, extension, folder_level2, folder_level3,
                                   folder_level4, "")
            # 3.封装实体

            # # 增,插入单行
            #  datainfo = DataArea(hostname='zs',ip_addr='333',port=22)
            #  session.add(u)

        self.ftp_Manager.close_connect()

    def insert_data_info(self, file_info, extension, date_str, location, url):
        """
        封装实体
        :param file_info:
        :param extension:
        :param date_str:
        :param location:
        :param url:
        :return:
        """
        size = self.ftp_Manager.size(file_info)
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').time()
        info = DataFileInfo(file_info, extension, date, size, location, url)


config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\Config.ini'
section = 'mysql'
data_service = DataService(config_path, section)
# fileinfo = data_service.get_file_info()
# data_service.save_files(fileinfo)




# -----------------测试ORM-------------------
config = data_service.ftp_Manager.get_config()
engine = create_engine("mysql+pymysql://" + config.get(section, 'username') + ":" + config.get(section, 'password') + "@localhost:3306/neargoos",
                        echo=True)

Session = sessionmaker(bind=engine)
session = Session()
ret = session.query(DataCategory).filter(DataCategory.is_delete < 1).all()
for item in ret:
    print(item.name)