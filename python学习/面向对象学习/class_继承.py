#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-19

__author__ = '@jiawenlong'


# class Father:  # 父类、基类
#
#     def basketball(self):
#         pass
#
#     def football(self):
#         pass
#
#     def smoke(self):
#         pass
#
#     def drink(self):
#         pass
#
#
# class Son(Father):  # 和 Father 建立 关系 ，即子类、派生类
#     def bj(self):
#         pass

#
# class F:
#     def f1(self):
#         print('F.f1')
#
#     def f2(self, name):
#         print('对 %s' % name)
#
#
# class F1:
#     def f3(self):
#         print('F.f3')
#
#
# class S(F, F1):
#     def s1(self, s):
#         print('%s' % s, end='')
#
#     def f2(self, name):
#         print('%s' % name)
#         # super(S, self).f1()  # 既执行子类方法，也执行父类相同方法
#         F.f2(self, name)  # 还可以这样执行父类方法
#
#
# s = S()
# s.s1("贾文龙")
# s.f2('是好人')


#  多继承 优先左边往上执行，如果有公用基类，先走左边，没有找到方法后，走右边执行，最终执行基类
# class F0:
#     def a(self):
#         print('F1.a')
#
#
# class F1(F0):
#     def a(self):
#         print('F1.a')
#
#
# class F2:
#     def a(self):
#         print('F2.a')
#
#
# class S(F1, F2):
#     pass
#
#
# obj = S()
# obj.a()


# 多继承例子
class Base:
    def __init__(self):
        print('Base.init')


class RequestHandler(Base):
    def __init__(self):
        Base.__init__(self)
        print('RequestHandler.init')


    def save_forever(self):
        print('RequestHandler.save_forever')
        person.process()  # self.process()

    def process(self):
        print('RequestHandler.process')


class Minx():
    def process(self):
        print('Minx.process')


class Son(Minx, RequestHandler):
    pass


person = Son()
person.save_forever()
