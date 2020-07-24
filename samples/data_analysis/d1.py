#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 9:18
# @Author  : brook-gaoyunfei
# @Site    : 
# @File    : d1.py
# @Software: PyCharm

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    for i in range(1, 101):
        if i % 2 == 0:
            return
            yield i



f = fibonacci(9999999999)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
