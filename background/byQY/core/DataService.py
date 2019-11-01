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

from background.byQY.core.FTPManager import FTPManager
from background.byQY.core.TimeUtil import TimeUtil


class DataService:
    def __init__(self, config_path, section):
        self.ftp_Manager = FTPManager(config_path, section)

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
        username = config.get(section, 'username')
        password = config.get(section, 'password')
        target = config.get(section, 'target')
        self.ftp_Manager.ftp_connect(host, username, password)
        file_infos = self.ftp_Manager.get_filename("", target)

        return file_infos

    def save_files(self, file_infos):
        """
        转存文件到指定目录，且将文件信息存入数据库的DataInfo表中
        [to-do]] 后续可将重复代码优化
        :param ftp_Manager:
        :param file_infos: 数据信息列表
        :return:
        """
    
        print(file_infos)
        i = 0
        for file_info in file_infos:
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
                # print(folder_level2 + folder_level3 + folder_level4)
                # print(file_info)
                # print('------------------')
                # 1.先将文件下载到本地
                # [to-do] linux下需修改
                local_path_dir = os.path.join('E:', r'\temp', folder_level1, folder_level2, folder_level3,
                                              folder_level4, "")
                remote_path_dir = '/'
                self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info, local_path_dir)
                print('下载浮标成功')
                # self.ftp_Manager.upload_file(local_path_dir+file_info, remote_newpath_dir + file_info)
                # print('上传成功')
            elif folder_level1 == 'STATION':
                folder_level2 = str(datetime.datetime.now().year)
                folder_level3 = file_info[0:2]
                folder_level4 = file_info[2:4]
                time = file_info[4:6]
                # UTC时间和系统时间调整
                if folder_level3 == '12' and folder_level4 == '31' and time > 16:
                    folder_level2 = folder_level2 + 1
                # 1.先将文件下载到本地
                # [to-do] Linux下需修改
                local_path_dir = os.path.join('E:', r'\temp', folder_level1, extension, folder_level2, folder_level3, folder_level4, "")
                remote_path_dir = '/'
                self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info, local_path_dir)
                print(local_path_dir)
                print('下载台站数据成功')
            elif folder_level1 == 'SHIP':
                folder_level2 = str(datetime.datetime.now().year)
                folder_level3 = file_info[2:4]
                folder_level4 = file_info[4:6]
                hour = file_info[6:8]
                # UTC时间和系统时间调整
                if folder_level3 == '12' and folder_level4 == '31' and int(hour) > 16:
                    folder_level2 = str(int(folder_level2) + 1)
                # 1.先将文件下载到本地
                # [to-do] Linux下需修改
                local_path_dir = os.path.join('E:', r'\temp', folder_level1, folder_level2, folder_level3,
                                              folder_level4, "")
                remote_path_dir = '/'
                self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info, local_path_dir)
                print('下载支援船数据成功')
        self.ftp_Manager.close_connect()

config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
section = 'neargoos'
data_service = DataService(config_path, section)
fileinfo = data_service.get_file_info()
data_service.save_files(fileinfo)

