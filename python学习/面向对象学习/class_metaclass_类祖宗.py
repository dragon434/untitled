#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-28

__author__ = '@jiawenlong'

'''python 一切皆对象'''

# class Foo:
#     def function(self):
#         print(123)


"""以上和下面的写法是相同的,都是声明了一个类"""


#
# def function(self):
#     print(123)
#
#
# Foo = type('Foo', (object,), {'func': function})


class Mytype(type):

    def __init__(self, *args, **kwargs):
        print(234)

    def __call__(self, *args, **kwargs):
        print(000)
        n = self.__new__(self)
        print(n)

#
class Foo(object, metaclass=Mytype):
    def __init__(self):
        print(123)

    def __call__(self, *args, **kwargs):
        print(111)

    def function(self):
        print(567)

    def __new__(cls, *args, **kwargs):
        return 111

obj = Foo()
# obj.function()
# obj()
