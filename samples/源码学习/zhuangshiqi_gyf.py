#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 15:07
# @Author  : brook-gaoyunfei
# @Site    : 
# @File    : zhuangshiqi_gyf.py
# @Software: PyCharm
def log_call(func):
    def handler(*args, **kwargs):
        print('start to call')
        result = func(*args, **kwargs)
        print('end of call')
        return result
    return handler

# def bar():
#     print('bar processing')
#
# bar = log_call(bar)
#
# bar()

@log_call
def bar():
    print('bar processing')

bar()