#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/28 15:18
# @Author  : yq
# @Site    : 
# @File    : FTPManager.py
# @Software: PyCharm
import ftputil
import configparser
config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
class FTPManager:
    # 获取配置文件信息，Section是大类，option为键
    def get_config_values(section, option):
        config = configparser.ConfigParser()
        config.read(config_path)
        return config.get(section=section, option=option)