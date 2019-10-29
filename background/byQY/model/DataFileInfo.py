#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/29 14:59
# @Author  : yq
# @Site    : 
# @File    : DataFileInfo.py
# @Software: PyCharm
#实体中间件
class DataFileInfo:
    def __init__(self, name, extensions, date, size, location, url):
        self.name = name
        self.extensions = extensions
        self.date = date
        self.size = size
        self.location = location
        self.url = url
