#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : @jia wen long


# 闭包
# def outer(x="哈哈哈哈"):
#     print("do something")
#     c = 10
#
#     def inner():
#         print(x, c)
#         # return x
#
#     return inner
#
#
# func = outer()
# func()


# 装饰器
import time


def showtime(func):
    def jtime():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("%s Spend %s" % (func.__name__, stop_time - start_time))
    return jtime


@showtime
def home():
    print("This is home Page")
    time.sleep(2)


def phone():
    print("This is phone Page")
    time.sleep(2)


@showtime
def jr():
    print("This is jr Page")
    time.sleep(2)


home()
print()
phone()
print()
jr()


# login_status = "False"
# username = "jiawenlong"
# password = "123456"
#
# def check_login():
#     print("out" % login_status)
#     def login():
#         global login_status
#         print(login_status)
#         if login_status != "True":
#             print(login_status)
#             login_status = "True"
#
#         #     user = raw_input("请输入用户名： ")
#         #     passwd = raw_input("请输入密码： ")
#         #     if user == username and passwd == password:
#         #         page()
#         #         login_status = "True"
#         #     else:
#         #         print("用户名密码错误！！")
#         # else:
#         #     page()
#     return login
#
#
# f=check_login()
# print(f())


# def foo(*args, **kwargs):
#     print 'args = ', args
#     print 'kwargs = ', kwargs
#     print '---------------------------------------'
#
#
# if __name__ == '__main__':
#     foo(1, 2, 3, 4)
#     foo(a=1, b=2, c=3)
#     foo(1, 2, 3, 4, a=1, b=2, c=3)
#     foo('a', 1, None, a=1, b='2', c=3)

# 装饰器练习
