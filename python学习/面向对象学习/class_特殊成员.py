#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-23

__author__ = '@jiawenlong'


class Foo:  # 特殊成员
    def __init__(self):
        print('init')

    def __int__(self):
        return 111

    def __str__(self):
        return 'jiawenlong'

    def __call__(self, *args, **kwargs):
        print('call', args, kwargs)


obj = Foo()  # 执行 init
obj(123, a=3, b='c')  # 执行 call
print(obj)  # print(str(obj)) 执行obj中的 __str__
print(int(obj))  # print(int(obj)) 执行obj中的 __int__

