#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-09

__author__ = '@jia wen long'

import configparser

config = configparser.ConfigParser()

# 配置DEFAULT模块
config["DEFAULT"] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
}

# 给 DEFAULT 添加一个配置
config['DEFAULT']['ForwardX11'] = 'yes'

# 也可以这样写
config['www.myconfigParser.com'] = {}
topsecret = config['www.myconfigParser.com']
topsecret['Port'] = '10086'
topsecret['ForwardX11'] = 'yes'

# 写入到文件
with open('example.ini', 'w') as configfile:
    config.write(configfile)




# import ConfigParser  # python2
#
# config = ConfigParser.ConfigParser()  # 创建配置文件对象，即配置文件文件描述符
#
# # python2 的写法
# fp = 'example.ini'
# config.read(fp)       # 打开conf
#
# # config.add_section('Section1')   #添加conf节点
# # config.set('Section1', 'name', 'jack')   #添加值
# # config.set('Section1', 'age', '23')
# # config.set('Section1', 'worker', 'CEO')
# # config.add_section('Section2')   #添加conf节点
# # config.set('Section2', 'name', 'rose')   #添加值
# # config.set('Section2', 'age', '21')
# # config.set('Section2', 'worker', 'CCC')
# # # with open(fp, 'w') as fw:   #循环写入
# # #     config.write(fw)
#
# # 读取
# name = config.get('Section1', 'name')
# age = config.get('Section1', 'age')
# print("name: %s \nage: %s" % (name, age))


# import os
# import sys

# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print os.path.abspath(__file__)
# print os.path.dirname(os.path.abspath(__file__))
# print base_dir


# +++++++++
# import confiParser  # python3
# 以下是 python3 的写法
# config = configParser.ConfigParser()  # 创建配置文件对象，即配置文件文件描述符
# 可以这样写
