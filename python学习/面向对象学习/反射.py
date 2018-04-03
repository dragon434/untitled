#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-04-02

__author__ = '@jiawenlong'


class Foo:
    stat = '123'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s" % (self.name, self.age)


obj = Foo('alex', 19)

# getattr 获取类对象成员的属性
b = "name"
# print(obj.__dict__[b])

# 去什么东西里面获取什么属性
# print(getattr(obj, "name"))
# print(getattr(obj, b))

# 获取类里的方法
# func = getattr(obj, "show")
# r = func()
# print(r)

# getattr(obj, "name") 获取对象属性
# hasattr(obj, 'name') 判断对象属性是否存在
# setattr(obj, 'k1', 'v1') 设置对象属性
# delattr(obj, 'name') 删除对象属性
# 通过字符串形式 操作对象中的成员


# r = getattr(Foo, 'stat')
# print(r)

'''
import s2


r1 = getattr(s2, 'Name')
print(r1)

r2 = getattr(s2, 'func')
print(r2)
v = r2()
print(v)

cls = getattr(s2, 'Foo')
print(cls)
print(obj)
obj = cls()
print(obj.name)
'''


# 例子
import s2
inp = input('请输入要查看的Url：')

if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')

