#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-08

__author__ = '@jiawenlong'

import logging

# One
# %(asctime)s     将日志的时间构造成可读的形式，默认情况下是精确到毫秒，如 2018-10-13 23:24:57,832
#                 可以额外指定 datefmt 参数来指定该变量的格式
# %(name)         日志对象的名称
# %(filename)s    不包含路径的文件名
# %(pathname)s    包含路径的文件名
# %(funcName)s    日志记录所在的函数名
# %(levelname)s   日志的级别名称
# %(levelno)s   数字形式的日志级别名称
# %(message)s     具体的日志信息
# %(lineno)d      日志记录所在的行号
# %(pathname)s    完整路径
# %(process)d     当前进程ID
# %(processName)s 当前进程名称
# %(thread)d      当前线程ID
# %(threadName)s  当前线程名称


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


# # Two
# logger = logging.getLogger("aaa")
# # logger = logging.getLogger()  # 创建日志对象
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('test.log')  # 创建一个handler，用于写入日志文件,文件对象
# ch = logging.StreamHandler()  # 创建一个handler 用于输出到屏幕，流对象
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 输出格式对象
#
# # 给文件对象和流对象创建输出格式
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 添加输出对象到日志对象
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 调用
# logger.debug(' this is debug message')
# logger.info(' this is info messages')
# logger.warning(' this is  warning messages')
# logger.error(' this is error messages')
# logger.critical(' this is critical messages')


# 第二次学习

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s %(name)s [行号:%(lineno)d] %(levelname)s  %(message)s %(levelno)s ',
#     # 以上圆括号中的变量不能改变，'行号' 是可以修改的
#     datefmt='%a %d %b %Y %H:%M:%S',
#     # datefmt 格式设置 datefmt="%d-%M-%Y %H:%M:%S"
#     # filename='test.log',
#     # filemode='a+'
#     )
# logging.debug('This is logiging.debug')
# logging.info('This is logiging.info')
# logging.warning('This is logiging.warning')
# logging.error('This is logiging.error')
# logging.critical("This is logging.critical")

logger = logging.getLogger()
file_h = logging.FileHandler('test.log')
scen_h = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s %(name)s [代码行号:%(lineno)d] %(levelname)s  %(message)s')

file_h.setFormatter(formatter)
# scen_h.setFormatter(formatter)

logger.addHandler(file_h)
logger.addHandler(scen_h)

logger.setLevel(logging.DEBUG)
logger.debug('This is logiging.debug')
logger.info('This is logiging.info')
logger.warning('This is logiging.warning')
logger.error('This is logiging.error')
logger.critical("This is logging.critical")
