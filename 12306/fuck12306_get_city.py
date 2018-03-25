#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2017-11-24

__author__ = '@jiawenlong'

import urllib2
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # 忽略证书认证

# 城市
city_uri = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9027'


def get_city_list():                           # 本函数 是生成器
    cities = urllib2.urlopen(city_uri).read()  # 访问城市的url获取城市的信息，是str
    cities = cities.split('=')[1]              # 分割字符串得到想要的城市信息和对应的代码，生成list，list的第二个元素就是城市信息和对应的代码
    cities = cities.split('|')                 # 对第二个信息再次分割，生成list，就是城市相关信息

    for i in range(len(cities)/5):             # 城市信息 5 个元素是一个城市，总共有 len(cities)/5 个城市
        city_name = cities[i * 5 + 1]
        city_code = cities[i * 5 + 2]
        yield city_name                        # 每组取出 i*5+1 和 i*5+2 这 2 个元素 就是城市对名称和对应对字母代码
        yield city_code


def get_city_code(city):
    cities_code = get_city_list()              # 创建生成器 并肤质给 cities_code
    for i in cities_code:                      # 对生成器进行循环  取出第一次的值 城市名称 如： 北京
        code = next(cities_code)
        if i == city:                          # 和函数传入的城市对比 如果相同 输出城市名称和代码
            # print city, code
            return code

# print get_city_code("天津")


















#
# def get_city_dic():                           # 本函数 最终返回字典
#     cities = urllib2.urlopen(city_uri).read()  # 访问城市的url获取城市的信息，是str
#     cities = cities.split('=')[1]              # 分割字符串得到想要的城市信息和对应的代码，生成list，list的第二个元素就是城市信息和对应的代码
#     cities = cities.split('|')                 # 对第二个信息再次分割，生成list，就是城市相关信息
#
#     for i in range(len(cities)/5):             # 城市信息 5 个元素是一个城市，总共有 len(cities)/5 个城市
#         city_name = cities[i*5+1]
#         city_code = cities[i*5+2]
#         yield city_name, city_code             # 每组取出 i*5+1 和 i*5+2 这 2 个元素 就是城市对名称和对应对字母代码
