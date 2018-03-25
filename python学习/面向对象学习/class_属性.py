#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-22

__author__ = '@jiawenlong'


# 属性的写法之一
# class province:
#     def __init__(self):
#         self.L = ['jiawenlong']
#     # 属性
#     @property   # 用于执行 obj.per
#     def per(self):
#         return self.L
#
#     @per.setter
#     def per(self, val):
#         self.L.append(val)
#         print(self.L)
#
#     @per.deleter
#     def per(self):
#         del self.L[1]
#         print(self.L)
#
# # 属性调用
# obj = province('aaa')
# # obj.per # print("Per")
# ret = obj.per
# print(ret)
# obj.per = 111
#
# del obj.per


# 属性的写法之二
class province1:
    # 属性
    def __init__(self):
        self.L = ['jiawenlong']

    def per(self):
        return self.L

    def set_per(self, val):
        self.L.append(val)
        print(self.L)

    def del_per(self):
        del self.L[1]
        print(self.L)

    p1 = property(fget=per, fset=set_per, fdel=del_per)


obj = province1()

ret = obj.p1
print(ret)
obj.p1 = 111
del obj.p1
