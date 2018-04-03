#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-04-02

__author__ = '@jiawenlong'

"""
class Foo:
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name,self.age)

# obj = Foo('ali', 19)  # obj 也叫实例
# obj1 = Foo('ali', 19)  # obj 也叫实例
# obj2 = Foo('ali', 19)  # obj 也叫实例
# obj3 = Foo('ali', 19)  # obj 也叫实例

# 单例，目的：永远使用同一份对象(实例)
v = None
while True:
    if v:
        v.show()
    else:
        v = Foo('Justin', 13)
        v.show()
"""

class Foo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

# 不要使用 类()
obj = Foo.get_instance()