#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/11/4 14:31
# @Author  : yq
# @Site    : 
# @File    : BaseDao.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from byQY.core.FTPManager import FTPManager


class BaseDao:

    def __init__(self, config_path, section):
        self.config_path = config_path
        self.section = section
        self.ftp_manager = FTPManager(config_path, section)
        self.config = self.ftp_manager.get_config()
        self.engine = create_engine(
            "mysql+pymysql://" + self.config.get(self.section, 'username') + ":" + self.config.get(self.section,
                                                                                         'password') + "@" + self.config.get(
                self.section, 'host') + self.config.get(self.section, 'dbName'),
            echo=True)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # def get_session(self):
    #     """
    #     获取Session
    #     :return:
    #     """
    #
    #     return session

    def find_all(self, model):
        """
        获取全部未被软删除的类型
        :param model: 数据的实体
        :return: 结果集
        """

        result = self.session.query(model).filter(model.is_delete < 1).all()
        return result

    def find_by_name(self, model, name):
        """
        获取名称相同的对象
        :param model: 数据的实体
        :param name: 匹配的名称
        :return: 结果集
        """

        result = self.session.query(model).filter_by(name=name).first()
        return result

    def find_by_url(self, model, url):
        """
        获取url相同的对象
        :param model: 数据的实体
        :param name: 匹配的名称
        :return: 结果集
        """

        result = self.session.query(model).filter_by(url=url).first()
        return result

    def insert_one(self, model):
        """
        写入一条数据
        :param model: 封装后的数据实体
        :return:
        """

        self.session.add(model)
        self.session.commit()
