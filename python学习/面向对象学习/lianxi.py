#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-04-08

__author__ = '@jiawenlong'

# class F1:
#     def __init__(self):
#         self.name = 123
#
#
# class F2:
#     def __init__(self, a):
#         self.ff = a
#
#
# class F3:
#     def __init__(self, b):
#         self.dd = b
#
#
# obj = F1()
# obj1 = F2(obj)
# obj2 = F3(obj1)
#
# r = obj2.dd.ff.name
# print(r)

"""
1. student
    1. course
    2. 
2. teacher
3. admin
"""


class School:
    payment = 0

    def __init__(self, course, address):
        self.course = course
        self.address = address

        # def create_grade(self, teacher):
        #     grade = self.course
        #     teacher = teacher


class Student:
    def __init__(self, name, phone, course):
        self.name = name
        self.phone = phone
        self.course = course
        # self.teacher = teacher

    def pay(self, money):
        School.payment += money
        return School.payment


class Course:
    def __init__(self, name, period, price, city):
        self.name = name
        self.cycle = period
        self.price = price
        self.school = city


class Teacher:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


#
# python = Course('python', 14, 2000)
# linux = Course('linux', 14, 2000)
# go = Course('go', 14, 2000)

# python_grade = School(python, '北京')
# linux_grade = School(linux, '北京')
# go_grade = School(go, '上海')

# li = Teacher('李杰', 28, 'python')
# zhang = Teacher('张杰', 38, 'linux')
# wang = Teacher('王杰', 29, 'go')

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

print('欢迎来到 坑死你 学校，这里你可以选择要学习的东西')
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
        print(School.payment)
    # 信息记录
    # student_info = open(student_name + '.info', 'a')
    # with open(student_name + '.json', 'a') as student_info:
    #     student_info.write()
else:
    exit()

# test = dict(name='justin', phone='xxxix', course='python', payment='yes')

