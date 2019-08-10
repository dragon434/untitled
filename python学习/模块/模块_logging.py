#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-08

__author__ = '@jiawenlong'

import logging

# One
# # 日志级别的配置
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                             # 周,天 月 年 时间
#                     filename='test.log',
#                     filemode='aw')
#
# logging.debug(' this is debug message')
# logging.info(' this is info messages')
# logging.warning(' this is  warning messages')
# logging.error(' this is error messages')
# logging.critical(' this is critical messages')


# Two
logger = logging.getLogger("aaa")
# logger = logging.getLogger()  # 创建日志对象
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')  # 创建一个handler，用于写入日志文件,文件对象
ch = logging.StreamHandler()  # 创建一个handler 用于输出到屏幕，流对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 输出格式对象

# 给文件对象和流对象创建输出格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 添加输出对象到日志对象
logger.addHandler(fh)
logger.addHandler(ch)

# 调用
logger.debug(' this is debug message')
logger.info(' this is info messages')
logger.warning(' this is  warning messages')
logger.error(' this is error messages')
logger.critical(' this is critical messages')
