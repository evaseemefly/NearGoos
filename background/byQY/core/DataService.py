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
def check_update(config_path, section, interval):
    ftp_Manager = FTPManager(config_path, section)
    # 获取配置文件信息
    config = ftp_Manager.get_config()
    host = config.get(section, 'host')
    username = config.get(section, 'username')
    password = config.get(section, 'password')
    target = config.get(section, 'target')
    ftp_Manager.ftp_connect(host, username, password)
    ftp_Manager.get_file_info_list(target)
    # 新建一个列表存储更新文件信息
    update_file_lists = []
    #过滤符合目标日期的文件
    # def file_filter(line):
    #     list=line.split()
    #     temp={}
    #     if






config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
section = 'neargoos'
interval = 1
check_update(config_path, section, interval)
