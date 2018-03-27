#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-23

__author__ = '@jiawenlong'

"""
class Foo:  # 特殊成员
    def __init__(self):
        print('init')

    def __int__(self):
        print(456)
        return 111

    def __str__(self):
        print('str')
        return 'jiawenlong'

    def __call__(self, *args, **kwargs):
        print('call', args, kwargs)


obj = Foo()  # 执行 init
obj(123, a=3, b='c')  # 执行 call

# print(obj)  # print(str(obj)) 执行obj中的 __str__ ; str(obj)
str(obj)
# r = str(obj)
# print(r)

# print(int(obj)) 执行obj中的 __int__ ; int(obj)
int(obj)
# r = int(obj)
# print(r)


__dict__(): # 将对象中封装的所有内容，通过字典的形式返回


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):   # 可以是减、乘除等
        # self = obj1 ('name', 19)
        # other = obj2 ('jiawenlong', 20)
        return self.age + other.age
        # return Foo(other.name, self.age)

    def __del__(self):  # 析构方法 对象被销毁时自动执行
        pass
        # print('析构方法')




obj1 = Foo('name', 19)
obj2 = Foo('jiawenlong', 20)

r = obj1 + obj2
# 两个对象相加，自动执行第一个对象的 __add__ 方法，并且将第二个对象作为参数传递进入
print(r) 
# print(r.name, r.age)

d = obj1.__dict__   # 将对象中封装的所有内容，通过字典的形式返回
print(d)
ret = Foo.__dict__
print(ret)
"""

