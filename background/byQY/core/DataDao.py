#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/11/1 18:55
# @Author  : yq
# @Site    : 
# @File    : DataDao.py
# @Software: PyCharm
class DataDao:

    def query_all_datainfo(self):
        results = session.query(user).filter_by(hostname='feng').all()
