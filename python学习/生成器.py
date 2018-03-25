#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2017-11-22

__author__ = '@jiawenlong'


def fib(fmax):
    n, before, after = 0, 0, 1

    while n < fmax:

        # print(before)
        # 生成器 标志 yield
        name = yield before

        print("My name is %s ! What is your name ?" % name)

        before, after = after, before + after

        n = n + 1


g = fib(6)
print(next(g))
g.send("jiawenlong")
