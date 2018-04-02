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
        print("遇到 class Foo 执行这个Mytype_init：%s" % 1)

    def __call__(self, *args, **kwargs):
        print("遇到 Foo() 执行  这个  Mytype_call: %s" % 2)
        n = self.__new__(self)
        print("然后创建对象，调用Foo的__new__创建对象：%s " % n)
        self.__init__(n)


# 下面2行是2.7的写法
# class Foo(object):
#     __metaclass__ = Mytype

class Foo(object, metaclass=Mytype):
    def __init__(self):
        print("最后执行，Foo_init: %s " % 4)

    def __call__(self, *args, **kwargs):
        print(111)

    def function(self):
        print(567)

    # obj 是在new中创建
    def __new__(cls, *args, **kwargs):
        return 3
        # return "对象" [obj]


obj = Foo()
# obj.function()
# obj()
