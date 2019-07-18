#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/7/15 21:57


# """
#     判断是否是素数
# """
#
# from math import sqrt
#
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
#
# if is_prime and num != 1:
#     print('%d 是素数' % num)
# else:
#     print('%d 不是素数' % num)

# print(int(sqrt(num)))


"""
    练习1
    百钱百鸡
    公鸡5元，母鸡3元，小鸡三只1元，一百元一百只鸡
    公鸡、母鸡、小鸡各多少
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡 %d 只 , 母鸡 %d 只, 小鸡 %d 只' % (x, y, z))


# a = 10
#
#
# def one():
#     # global a
#     print(a)   # UnboundLocalError: local variable 'a' referenced before assignment 未分配的本地错误：局部变量a在赋值前引用了
#     a = 100
#     print(a)
#
#
# one()
# print(a)
