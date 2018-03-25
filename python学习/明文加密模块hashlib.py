#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-07

__author__ = '@jiawenlong'

import hashlib

db = {
    'username': '2c9d18ba9ed23b6da92e6ec471d1805b',  # jiawenlong
    'pass': 'e10adc3949ba59abbe56e057f20f883e'  # 123456
}


# h = hashlib.md5()
# h.update('jiawenlong')
# h.update('123456')
# print "mima:", h.hexdigest()

# h.update('123456'.encode('utf8')) ### python3 中必须对字符串进行转换
# python3 字符串是以unicode方式存在内存的，需要encode转换为字节类型


def get_md5(s):
    hashs = hashlib.md5()
    hashs.update(s.encode('utf8'))
    return hashs.hexdigest()


# def login(user, password):
#
#     '''以下这种加密方式是在用户名的基础上，又对密码进行加密'''
#
#     print "密码：", password
#     hash = hashlib.md5()
#     hash.update(user)
#     user = hash.hexdigest()
#     print
#     hash.update(password)
#     password = hash.hexdigest()
#     print "密码：", password
#     if user == db['username']:
#         if password == db['pass']:
#             print "登陆成功"
#         else:
#             print "用户名或密码错误"
#     else:
#         print "用户名或密码错误"


def login(username, password):
    """函数调用加密，是分别加密，和上面的方式得到的密码是不同的"""
    user = get_md5(username)
    print()
    password = get_md5(password)
    if user == db['username']:
        if password == db['pass']:
            print("登陆成功")
        else:
            print("用户名或密码错误")
    else:
        print("用户名或密码错误")


user = input("请输入用户名：_> ")
paword = input("请输入密码：_> ")

login(user, paword)
