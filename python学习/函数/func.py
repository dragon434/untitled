#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/7/8 22:19


def logger(log_text):
    f = open("test.log", 'a')
    f.write(log_text)
    f.close()
    print(log_text)


# logger('Hello')


# subroutine 【子程序】 , procedures 【过程】   函数
# 作用： 减少重复代码、方便修改、更易扩展、保持代码一致性

def f(**kwargs):
    print(kwargs)


zd = {'name': 'Jiawenong', "age": 31}

f(**zd)
f(**{'IP': '11.12.13.14', 'LocalName': 'Uinnova_Tarsier'})
# ** 后面直接跟json格式字符串

