#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import datetime
import random
from dateutil import parser

print "列表合并"
l1 = ['a', 'b']
l2 = [1, 2]
print("L1:%s" %l1 , "L2:%s" %l2)
print dict([l1, l2])
print dict(zip(l1, l2))


print('')
print("随机数：")
time.sleep(1)
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.random())

print('')
print("时间模块")
print('时间模块 天/月/年:%s' % (datetime.date.today()).strftime('%d/%m/%Y'))
print('时间模块 年-月-日:%s' % (datetime.date.today()).strftime('%Y-%m-%d'))
myDT = datetime.date(2017, 8, 2)
print(myDT.strftime('%Y-%m-%d'))
print time.ctime(time.time())
print time.asctime(time.localtime(time.time()))
dt1 = time.asctime(time.gmtime(time.time()))
dt = parser.parse(dt1)
print dt

print('')
print('字符串长度')
s = 'strlen'
print "strlen:", len(s)
print("strlen:", len(s))
#st = raw_input('pleaer input a string:')
st="1234"
print "st:", len(st)
print "the string st has %d characters" % len(st)




timbitsLeft = int(input("输入购买个数：")) # 步骤1: 得到输入
totalCost = 0              # 步骤2: 设定总计

# 步骤3: 尽可能地多买大盒子
if timbitsLeft >= 40:
   bigBoxes = int(timbitsLeft / 40)
   totalCost = totalCost + bigBoxes * 6.19    # 更新总计
   timbitsLeft = timbitsLeft - 40 * bigBoxes  # 仍需计算timbits
if timbitsLeft >= 20:
    bigBoxes = int(timbitsLeft / 20) # 步骤4, 我们能购买一个中盒子么?
    totalCost = totalCost + 3.39
    timbitsLeft = timbitsLeft - 20
if timbitsLeft >= 10:
    bigBoxes = int(timbitsLeft / 10)# 步骤5, 我们能购买一个小盒子么?
    totalCost = totalCost + 1.99
    timbitsLeft = timbitsLeft - 10
if timbitsLeft >= 1:
    totalCost = totalCost + 0.20
    timbitsLeft = timbitsLeft - 1

totalCost = totalCost + timbitsLeft * 0.2 # 步骤6
print("总计需要：%s"  % totalCost)


def middle(L):
   Longth=len(L)
   mid=int(Longth//2)
   print(L[mid])

middle([1,2,3,4,51,4,10,30])

