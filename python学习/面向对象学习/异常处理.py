#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-30

__author__ = '@jiawenlong'


"""
try:
    # 代码块
    i = int('1')
except IndexError as e:
    print("IndexError", e)
except ValueError as e:
    print("ValueError", e)
except Exception as e:
    # 上述代码如果出错，自动执行当前块
    # e 是 Exception的对象，对象中封装错误信息
    print("Exception", e)
else:
    print("else")
finally:
    print('finally')
"""

try:
    raise Exception('主动触发异常')
except Exception as e:
    print(e)

def db():
    return False

def index():
    try:
        resault = db()
        if not resault:
            raise Exception('')