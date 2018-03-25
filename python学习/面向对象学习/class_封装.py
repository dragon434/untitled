#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-19

__author__ = '@jiawenlong'

'''
面向对象，三大特性
1. 封装
2. 继承
3. 多态
'''


# class one:
#     def echo(self, info):
#         print("%s, %s, %s, %s" % (self.name, self.age, self.sex, info))
#
#
# o = one()
# o.name = '小明'
# o.age = 19
# o.sex = '男'
# o.echo("上山去打柴")
# o.echo('最爱大保健')
# o.echo('开车去东北')
#
# print()
#
# o.name = '老张'
# o.age = 40
# o.sex = '男'
# o.echo("上山去打柴")
# o.echo('最爱大保健')
# o.echo('开车去东北')

# 构造方法
class one:
    def __init__(self, name, age, sex):
        """
        构造方法
        """
        self.name = name
        self.age = age
        self.sex = sex

    def echo(self, info):
        print("%s, %s, %s, %s" % (self.name, self.age, self.sex, info))


xm = one("小明", 19, '男')
lz = one("老张", 40, '女')

xm.echo("上山去打柴")
xm.echo('最爱大保健')
xm.echo('开车去东北')
print()
lz.echo("上山去打柴")
lz.echo('最爱大保健')
lz.echo('开车去东北')
