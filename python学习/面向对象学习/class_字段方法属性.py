#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-20

__author__ = '@jiawenlong'


class province:
    # 静态字段
    country = '中国'

    def __init__(self, name):
        # 普通字段
        self.name = name
        self.L = ['jiawenlong']

    # 普通方法
    def bar(self):
        print('Bar')

    # 静态方法
    @staticmethod
    def sta(name, age):
        print(name, age)

    # 类方法
    @classmethod
    def classmd(cls):
        # cls 类名
        print('classmd')

    # 属性
    @property  # 用于执行 obj.per
    def per(self):
        return self.L

    @per.setter
    def per(self, val):
        self.L.append(val)
        print(self.L)

    @per.deleter
    def per(self):
        del self.L[1]
        print(self.L)


"""
# 静态字段使用
print(province.country)

hn = province('河南')
print(hn.name)

hn.name = "河南男"
print(hn.name)

hb = province('河北')
hb.country = '美国'
print(hb.country, hb.name)

# 普通方法调用
obj = province('hh')
obj.bar()
obj.sta(1, 2)
obj.classmd()
#
# 静态方法调用 节省内存
province.sta(1, 2)

# 类方法调用 节省内存
province.classmd()
"""

# 应用场景
# 1 如果对象中需要保存一些值，执行某功能时，需要使用对象中的值 --- 使用普通方法
# 2 不需要任何对象中的值 --- 使用静态方法

# 属性调用
obj = province('aaa')
# obj.per # print("Per")
ret = obj.per
print(ret)
obj.per = 111

del obj.per
