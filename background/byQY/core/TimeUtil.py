#!/usr/bin/env python

# encoding: utf-8

# @Time    : 2019/10/30 16:09
# @Author  : yq
# @Site    : 
# @File    : TimeUtil.py
# @Software: PyCharm

import time
import datetime


class TimeUtil:
    @staticmethod
    def utc2local(utc_st):
        """UTC时间转本地时间（+8: 00）"""
        now_stamp = time.time()
        local_time = datetime.datetime.fromtimestamp(now_stamp)
        utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
        offset = local_time - utc_time
        local_st = utc_st + offset
        return local_st

    @staticmethod
    def local2utc(local_st):
        """本地时间转UTC时间（-8: 00）"""
        time_struct = time.mktime(local_st.timetuple())
        utc_st = datetime.datetime.utcfromtimestamp(time_struct)
        return utc_st
