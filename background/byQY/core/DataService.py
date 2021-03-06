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
import BaseDao
import FTPManager
import DataModel
from apscheduler.schedulers.blocking import BlockingScheduler
global config_path
config_path = r'E:\projects\pycharm\NearGoos\background\byQY\config\Config.ini'
global section_neargoos
section_neargoos = 'neargoos'
global section_mysql
section_mysql = 'mysql'
class DataService:
    def __init__(self, config_path, section_neargoos, section_mysql):
        self.ftp_Manager = FTPManager.FTPManager(config_path, section_neargoos)
        self.username = ""
        self.password = ""
        self.config_path = config_path
        self.section_neargoos = section_neargoos
        self.section_mysql = section_mysql
        self.dao = BaseDao.BaseDao(config_path, section_mysql)

    @staticmethod
    def switch_category(value):
        """
        根据后缀解析数据类型
        :param value: 后缀名
        :return: 数据类型
        """
        switcher = {
            "xml": "BUOY",
            "bbx": "SHIP",
            "FUB": "IGNORE_DATA"
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

        # 获取时间
        # self.ftp_Manager.getCreateTime()
        file_infos = self.ftp_Manager.get_filename("", target)

        return file_infos

    def save_files(self, file_infos):
        """
        转存文件到指定目录，且将文件信息存入数据库的DataInfo表中
        [to-do]] 后续可将重复代码优化
        :param file_infos: 数据信息列表
        :return:
        """
        # 1. 在遍历文件列表前先查出海区，类型，数据源对应ID
        # [to-do]暂时只要类型
        # 1.1 [to-do]得到对应的海区ID（暂时均为默认海区）
        area_result = self.dao.find_by_name(DataModel.DataArea, 'China Sea')
        # 1.2 [to-do]得到数据源的ID（暂时均为中国）
        source_result = self.dao.find_by_name(DataModel.DataSource, 'China')
        # 1.3 [to-do]得到数据类型的ID
        category_result = self.dao.find_all(DataModel.DataCategory)
        dict_category = dict()
        for obj in category_result:
            dict_category[obj.name] = obj.id
        num_database = 0
        num_savefile = 0
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

            if folder_level1 == 'BUOY':
                # 2.2 三级目录文件名（年）
                folder_level2 = file_info[0:4]
                # 2.3 四级目录文件名（月）
                folder_level3 = file_info[4:6]
                # 2.4 五级目录文件名（日）
                folder_level4 = file_info[6:8]
                hour = file_info[8:10]
                # [to-do] 暂时只有一个浮标，以后增加时需要修改
                extension = 'QD'
            elif folder_level1 == 'STATION':
                str_year = str(datetime.datetime.now().year)
                str_month = str(datetime.datetime.now().month)
                str_day = str(datetime.datetime.now().day)

                folder_level2 = self.ftp_Manager.getCreateTime('/' + file_info)
                # folder_level2 = str(datetime.datetime.now().year)

                folder_level3 = file_info[0:2]
                folder_level4 = file_info[2:4]
                # 如果大于当前日期，年份减1
                str_ob_date = folder_level2 + '-' + folder_level3 + '-' + folder_level4
                ob_date = datetime.datetime.strptime(str_ob_date, '%Y-%m-%d')
                if ob_date > datetime.datetime.now():
                    folder_level2 = str(int(folder_level2) - 1)
                print(str(datetime.datetime.now()) + '获取时间:' + str(ob_date))
                hour = file_info[4:6]
                # # UTC时间和系统时间调整
                # if folder_level3 == '12' and folder_level4 == '31' and hour > '16':
                #     folder_level2 = str(int(folder_level2) + 1)

            elif folder_level1 == 'SHIP':
                folder_level2 = str(datetime.datetime.now().year)
                folder_level3 = file_info[2:4]
                folder_level4 = file_info[4:6]
                hour = file_info[6:8]
                # [to-do] 暂时只有一个志愿船，以后增加时需要修改
                extension = 'default'
                # # UTC时间和系统时间调整
                # if folder_level3 == '12' and folder_level4 == '31' and int(hour) > 16:
                #     folder_level2 = str(int(folder_level2) + 1)
            elif folder_level1 == 'IGNORE_DATA':
                print("FUB后缀文件不下载")
                continue
            # 3.先将文件下载到本地
            # [to-do] Linux下需修改
            local_path_dir = os.path.join('E:', r'\projects\pycharm\NearGoos\webclient\public', folder_level1, extension, folder_level2, folder_level3,
                                          folder_level4, "")
            remote_path_dir = '/'
            is_success = self.ftp_Manager.download_file(local_path_dir + file_info, remote_path_dir + file_info,
                                                        local_path_dir)

            if is_success:
                num_savefile += 1

                date_str = folder_level2 + '-' + folder_level3 + '-' + folder_level4 + ' ' + hour + ':' + '00' + ':' + '00'
                url = os.path.join(folder_level1, extension, folder_level2, folder_level3,
                                   folder_level4, file_info)
                # 4.封装实体
                result = self.dao.find_by_url(DataModel.DataDataInfo, url)
                if result is None:
                    self.insert_data_info(file_info, folder_level1, extension, date_str, url, area_result, dict_category, source_result,local_path_dir + file_info)
                    print('向数据库存储成功')
                    num_database += 1

                else:
                    print('!!!!!!该文件信息已在数据库中存在')
        self.ftp_Manager.close_connect()
        print('静态文件总共存储了' + str(num_savefile))
        print('数据库总共存储了' + str(num_database))
    def insert_data_info(self, file_info, folder_level1, extension, date_str, url, area_result, dict_category, source_result,local_dir):
        """
        封装实体
        :param file_info:
        :param extension:
        :param date_str:
        :param location:
        :param url:
        :return:
        """
        # # 4.1 [to-do]得到对应的海区ID（暂时均为默认海区）
        # area_result = self.dao.find_by_name(DataArea, 'China Sea')
        # # 4.2 [to-do]得到数据源的ID（暂时均为中国）
        # source_result = self.dao.find_by_name(DataSource, 'China')
        # # 4.3 [to-do]得到数据类型的ID（暂时均为中国）
        # category_result = self.dao.find_by_name(DataCategory, folder_level1)
        datainfoModel = DataModel.DataDataInfo()
        info = DataModel.DataDataInfo()
        info.is_delete = 0
        info.gmt_create = datetime.datetime.now()
        info.gmt_modified = datetime.datetime.now()
        info.name = file_info
        info.extensions = extension
        # [to-do]暂时没有备注
        # 使用date类型传入MySQL数据库
        info.date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        info.area_id = area_result.id
        info.category_id = dict_category.get(folder_level1)
        info.source_id = source_result.id
        info.url = url
        # [to-do]暂时没有FTP文件的最新修改日期
        info.size = os.path.getsize(local_dir)
        info.location = extension
        self.dao.insert_one(info)


    def getTime(self):
        self.ftp_Manager.getCreateTime(self)




#主任务
def task():
    data_service = DataService(config_path, section_neargoos, section_mysql)
    fileinfo = data_service.get_file_info()
    data_service.save_files(fileinfo)

# 定时任务
def scheduleTask():
    times = 0;
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(task, 'interval', seconds=60, id='task1')
    scheduler.start()



scheduleTask()






