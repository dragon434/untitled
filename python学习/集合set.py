#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/7/8 21:32




# print(set('alex') == set('alexexex'))
# print(set("alex") < set('alexw'))


# print('Set And: ', set('alex') and set('alexw'))
# print('Set Or', set('alex') or set('alexw'))


# a = set([1, 2, 3, 4, 5])
a = set([4, 5])
b = set([4, 5, 6, 7, 8])

print('交集', a.intersection(b))
print('交集&', a & b)

print('并集', a.union(b))
print('并集|', a | b)

print('差集', a.difference(b))
print('差集-', a - b)

print('差集', b.difference(a))
print('差集-', b - a)

print('对称差集', a.symmetric_difference(b))  # 除了相同的，其他的取出来
print('对称差集^', a ^ b)

print('子集', a.issubset(b))  # a 是否是 b 的子集
print('子集 <', a < b)
print('超集/父集', a.issuperset(b))  # a 是否完成包含 b
print('超集/父集>', a > b)
