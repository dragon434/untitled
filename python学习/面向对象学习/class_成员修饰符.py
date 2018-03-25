#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-23

__author__ = '@jiawenlong'

"""
# 私有字段，私有静态字段
class Foo:
    __country = "__中国"  # 私有静态字段
    country = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__age = age  # 私有字段 外部无法字节访问 ；__ 成员修饰符

    # 私有字段的调用
    def show(self):
        return self.__age

    # 私有静态字段的调用
    def show_country(self):
        return Foo.__country

    @staticmethod
    def show2_country():
        return Foo.__country


obj = Foo('jiawenlong', 19)

# 普通字段引用
print(obj.name)
print(obj.age)
# 私有字段引用
ret = obj.show()
print(ret)

# 静态字段引用
print(Foo.country)
# print(obj.country)
# 私有静态字段引用
ret = obj.show_country()
print(ret)

# 静态方法用于待用私有静态字段
print(Foo.show2_country())
"""

'''
# 方法的私有化
class Foo:
    def __f1(self):
        return 123

    def f2(self):
        r = self.__f1()
        return r


obj = Foo()
ret = obj.f2()
print(ret)
'''


# 继承的私有,私有无法继承
class F:
    def __init__(self):
        self.__gr = 123
        self.gr = 456

    def showm(self):
        return self.__gr


class S(F):
    def __init__(self, name):
        self.name = name
        self.__age = 18
        super(S, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.gr)
        print(self.showm())


s = S('jiawenlong')
s.show()
