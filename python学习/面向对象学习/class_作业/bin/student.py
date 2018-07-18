#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-04-08

__author__ = '@jiawenlong'

import json
import os
import sys
sys.path.append('..')
# Conf_path = sys.path
from lianxi import *

school_course = {
    'python': {
        'period': 14,
        'price': 2000,
        'city': '北京'
    },
    'linux': {
        'period': 18,
        'price': 2500,
        'city': '北京'
    },
    'go': {
        'period': 20,
        'price': 3000,
        'city': '上海'
    }
}

print('欢迎来到 坑死你 学校，这里你可以选择要学习的课程')
print('目前我们开设了3门课程，python、linux、go')
print('他们分别在 北京和上海开课，详细信息请查询')

while True:
    student_course = input('\n请输入你要学的的课程可以查看详细信息：')

    # print(school_course[student_course]['period'])
    if student_course != 'python' and student_course != 'go' and student_course != 'linux':
        print('抱歉，我们学校没有您要查询的课程，请重新选择')
        continue
    # 课程
    course = Course(student_course, school_course[student_course]['period'], school_course[student_course]['price'],
                    school_course[student_course]['city'])
    print('以下是 %s 课程的详细信息：\n学习地址：%s\n课程名称: %s\n周期: %s周\n价格[人民币]: %s' %
          (course.name, course.school, course.name, course.cycle, course.price))
    goon = input('是否继续查询[y/n]：')
    if goon == 'y' or goon == 'Y':
        continue
    else:
        break

register = input('\n是否现在注册[y/n]：')
if register == 'y' or register == 'Y':
    student_name = input('请输入你的名字：')
    student_pwd = input('请输入您的密码：')
    student_phone = input('请输入您的手机号：')
    student_course = input('请输入要学习的课程: ')
    # 学生注册
    course = Course(student_course, school_course[student_course]['period'], school_course[student_course]['price'],
                    school_course[student_course]['city'])
    student_one = Student(student_name, student_phone, course)
    print('你的名字是：%s, 手机号: %s \n\n你所选的课程的详细信息：\n学习地址：%s\n课程名称: %s\n周期: %s周\n价格[人民币]: %s'
          % (student_name, student_phone, course.school, course.name, course.cycle, course.price))
    register = input('\n是否现在付款[y/n]：')
    if register == 'Y' or register == 'y':
        money = int(input('请支付：'))
        ret = student_one.pay(money)
        print('您的付款 %s ，我们已经收到，后续会有专员跟您联系，感谢选择坑死你学校进行培训！' % ret)
        # print(School.payment)
        # 信息记录
        # student_info = open(student_name + '.info', 'a')
        json = json.dumps({'name': student_name, 'passwd': student_pwd, 'phone': student_phone,
                           'course': student_course, 'payment': 'yes', 'city': course.school})
        with open(student_name + '.json', 'w') as student_info:
            student_info.write(json)
    else:
        exit()
else:
    name = input('请输入登陆名: ')
    pswd = input('请输入密码:')
    if os.path.exists(name + '.json'):
        with open(name + '.json', 'r') as f:
            student = json.load(f)
            # print(student)
            if name == student['name'] and pswd == student['passwd']:
                print('\n您选的课程是: %s\n地址在: %s\n是否付款：%s' % (student['course'], student['city'], student['payment']))
                exit()
    else:
        print('\n用户名密码错误')