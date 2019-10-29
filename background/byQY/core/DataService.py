#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/28 18:14
# @Author  : yq
# @Site    : 
# @File    : DataService.py
# @Software: PyCharm
# 连接FTP
from background.byQY.core.FTPManager import FTPManager
#根据后缀名解析数据类型
def switch_category(value):
    switcher = {
        "xml": "FUB",
        "bbx": "SHIP"
    }
    return switcher.get(value, 'STATION')


# 根据指定间隔查询更新
def get_file_info(config_path, section, interval):
    ftp_Manager = FTPManager(config_path, section)
    # 获取配置文件信息
    config = ftp_Manager.get_config()
    host = config.get(section, 'host')
    username = config.get(section, 'username')
    password = config.get(section, 'password')
    target = config.get(section, 'target')
    ftp_Manager.ftp_connect(host, username, password)
    # file_info = ftp_Manager.get_file_info_list(target)
    # for modify in file_info:
    #     print(modify.strip(), end='!')

    file_infos = ftp_Manager.get_filename("", target)
    for file_info in file_infos:
        extension = file_info[-3:]
    #一级目录文件名
        folder_level1 = switch_category(extension)
    #二级目录文件名
        if folder_level1 == 'FUB':
            folder_level2 = file_info[0:4]
            folder_level3 = file_info[4:6]
            folder_level4 = file_info[6:8]
            print(folder_level2+folder_level3+folder_level4)
            print(file_info)
            print('------------------')













config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\ftpConfig.ini'
section = 'neargoos'
interval = 1
fileinfo = get_file_info(config_path, section, interval)
