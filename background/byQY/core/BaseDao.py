#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/11/4 14:31
# @Author  : yq
# @Site    : 
# @File    : BaseDao.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from background.byQY.core.FTPManager import FTPManager


class BaseDao:

    def __init__(self, config_path, section):
        self.config = config_path
        self.section = section

    def get_session(self):
        """
        获取Session
        :return:
        """
        ftp_manager = FTPManager(self.config_path, self.section)
        config = ftp_manager.get_config()
        engine = create_engine(
            "mysql+pymysql://" + self.config.get(self.section, 'username') + ":" + self.config.get(self.section,
                                                                                              'password') + "@" + self.config.get(
                self.section, 'host') + self.config.get(self.section, 'dbName'),
            echo=True)

        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def find_all(self, model):
        """
        获取全部未被软删除的类型
        :param model: 数据的实体
        :return: 结果集
        """
        session = self.get_session()
        result = self.session.query(model).filter(model.is_delete < 1).all()
        return result

    def find_by_name(self, model, name):
        """
        获取名称相同的对象
        :param model: 数据的实体
        :param name: 匹配的名称
        :return: 结果集
        """
        session = self.get_session()
        result = self.session.query(model).filter_by(name=name).first()
        return result

    def insert_one(self, model):
        """
        写入一条数据
        :param model: 封装后的数据实体
        :return:
        """
        session = self.get_session()
        self.session.add(model)
        self.session.commit()
