#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/11/1 18:55
# @Author  : yq
# @Site    : 
# @File    : DataCategoryDao.py
# @Software: PyCharm
# from background.byQY.core.BaseDao import BaseDao
# from background.byQY.model.DataModel import DataCategory
#
#
# class DataCategoryDao(BaseDao):
#     def get_all_category(self):
#         """
#         获取全部未被删除的数据类型
#         :return:
#         """
#         result = self.session.query(DataCategory).filter(DataCategory.is_delete < 1).all()
#         return result
