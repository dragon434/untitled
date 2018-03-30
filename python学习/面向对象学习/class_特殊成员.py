#!/usr/bin/env python
# -*- coding:utf-8 -*-
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


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        # return item + 10
        if type(item) == slice:  # li[1:2:3]
            print('\n进行切片处理')
            print('start: %s' % item.start)
            print('end: %s' % item.stop)
            print('step: %s\n' % item.step)
        else:
            print('进行索引处理')
            print(item, type(item))

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


li = Foo('jia', 19)
r = li[8]   # 自动执行li对象的类中的 __getitem__ 方法，8 当参数传递给 item
# print(r)
li[1:3:2]

li[100] = 'haha'
del li[999]
"""

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        # return iter([11, 22, 33, 44])
        return [11, 22, 33, 44]


li = Foo('Justin', 19)
# 1 执行 li 对象的类中的 __iter__方法，并获取其返回值
# 2 循环上一步中的返回对象

# 如果类中 有 __iter__ 方法，创建的对象就是可迭代对象
# 对于  可迭代对象.__iter__() 的返回值 是 迭代器
# 对于  for 循环，遇到迭代器，执行迭代器的next方法 ; iter([11, 22, 33, 44]) 迭代器
# 如果是可迭代对象，获取对象的 __iter__方法，然后执行迭代器的next方法 ；def __iter__(): return [11, 22, 33, 44],  可迭代对象
a = li.__iter__()
print(type(a))

b = [1, 2, 3]
print(type(b))

for i in li.__iter__():
    print(i)


















