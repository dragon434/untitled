#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : @jiawenlong


login_status = "False"
username = "jiawenlong"
password = "123456"

wxusername = "wx"
wxpassword = "123456"

import time


def input_name(auth, name, pwd, page, *x, **y):
    user = input("请输入 %s 用户名： " % auth)
    passwd = input("请输入 %s 密码： " % auth)
    if user == name and passwd == pwd:
        page(*x, **y)
    else:
        print("\n账号密码输入错误，请重新输入")
        input_name(auth, name, pwd, page, *x, **y)


def max_login(auth="jd"):  ## 装饰器参数
    def check_login(page):  ### 装饰器函数
        def login(*x, **y):
            global login_status
            if login_status != "True":
                if auth == "jd":
                    input_name(auth, username, password, page, *x, **y)
                    login_status = "True"
                elif auth == "wx":
                    input_name(auth, wxusername, wxpassword, page, *x, **y)
                    login_status = "True"
            else:
                page(*x, **y)

        return login

    return check_login


@max_login("wx")
def home(*x, **y):
    print("\nThis is home page....")
    page_name = " "
    for i in x:
        page_name = i + " " + page_name
    print("I Have All The Class :")
    print("They ware %s ......\n" % page_name)


@max_login("jd")
def jr(*x, **y):
    print("\nThis is jr page")
    page_name = " "
    for i in x:
        page_name = i + " " + page_name
    print("I Have All The JinRong Class: ")
    print("They ware %s .....\n" % page_name)


@max_login()
def phone(*x, **y):
    page_name = " "
    print("\nThis is Phone Page......")
    for i in x:
        page_name = i + " " + page_name
    print("You Can search All Class of Phone: ")
    print("They ware %s ......\n" % page_name)


print("\nThis home Page \n")
htm = "home"
while True:
    print("\n当前您在 home 页面,还可以进入的页面是：jr home phone OR exit 退出")
    htm = input("---> ")
    if htm == "jr":
        jr("基金理财", "京东理财", "京东E卡")
    elif htm == "home":
        home("京东金融", "手机", "服装", "超市")
    elif htm == "phone":
        phone("华为", "三星", "小米", "荣耀", "iphone")
    elif htm == "exit":
        exit()
    else:
        print("\n您想进入的页面正在建设中，请重新选择！！！,5秒后自动跳转 home 页面！！！！！")
        time.sleep(5)
