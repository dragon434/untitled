#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-04-08

__author__ = '@jiawenlong'


# import json
# import os
# import sys
# sys.path.append('..')
# # Conf_path = sys.path
# from lianxi import *



def digitalSum(n):
    if n == 0:
        return n
    return digitalSum(n//10) + n%10

# print(digitalSum(19))

def digitalRoot(n):
    return digitalSum(digitalSum(digitalSum(digitalSum(n))))


# print(digitalRoot(99909876541234556789098734567896543678909999999912345678901999123456789099999999))


def hailstone(n):
    if n % 2 == 0:
        print(n)
        hailstone(n//2)
    if n == 1:
        print(n)
        exit()
    else:
        print(n)
        hailstone(3*n+1)


hailstone(15)