#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 8:56
# @Author  : brook-gaoyunfei
# @Site    : 
# @File    : tcp_stat_gyf.py
# @Software: PyCharm
from collections import defaultdict

stat_names = {
    '0A': 'LISTEN',
    '01': 'ESTABLISHED',
    # ...
}

# 遍历每个连接，按连接状态累加
stats = defaultdict(int)

with open(r'C:\Users\gaoyunfei_t\PycharmProjects\learn-python3\samples\源码学习\tcp') as f:
    # 跳过表头行
    f.readline()

    for line in f:
        st = line.strip().split()[3]
        print('st:',st,type(st))
        stats[st] += 1
print('stats:',stats)
print('items:',stats.items())
for st, count in stats.items():
    print('st:',st,'count:',count,stat_names[st], count)
