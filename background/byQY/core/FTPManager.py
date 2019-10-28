#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/28 15:18
# @Author  : yq
# @Site    : 
# @File    : FTPManager.py
# @Software: PyCharm
import ftputil
import configparser
import time
from ftplib import FTP


# config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
class FTPManager:
    def __init__(self, config_path, section):
        self.config_path = config_path
        self.ftp = FTP()
        self.section = section

    # 连接FTP
    def ftp_connect(self, host, username, password):
        self.ftp.connect(host)
        self.ftp.login(username, password)

    # 显示ftp指定目录下的文件,详细信息 ------- ftp.cat_dir()
    def get_file_info_list(self, filepath):
        self.ftp.cwd(filepath)
        file_list = self.ftp.retrlines('RETR')
        print(file_list)
        return file_list

    # 获取配置文件信息
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        return config

    # 关闭连接
    def close_connect(self):
        self.ftp.close()


    # # 获取指定间隔内的文件更新
    # def check_update(self, section):
    #     currenttime = time.time()
    #     print("current new time is", time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()))
    #
    #     host = config.get(section, 'host')
    #     username = config.get(section, 'username')
    #     password = config.get(section, 'password')
    #     # 连接数据库
    #     self.ftp_connect(host, username, password)
    #     self.cat_dir(config.get(section, 'target'))


# test = FTPManager(r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini')
# test.check_update('neargoos')