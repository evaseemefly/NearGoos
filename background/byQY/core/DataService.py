#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/28 18:14
# @Author  : yq
# @Site    : 
# @File    : DataService.py
# @Software: PyCharm
# 连接FTP
from background.byQY.core.FTPManager import FTPManager


# 根据指定间隔查询更新
def check_update(config_path, section):
    ftp_Manager = FTPManager(config_path, section)
    # 获取配置文件信息
    config = ftp_Manager.get_config()
    host = config.get(section, 'host')
    username = config.get(section, 'username')
    password = config.get(section, 'password')
    ftp_Manager.ftp_connect(host, username, password)
    cat = ftp_Manager.cat_dir(config.get(section, 'target'))
    print(cat)


config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
section = 'neargoos'
check_update(config_path, section)