#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2017-11-27

__author__ = '@jiawenlong'

import urllib2
import urllib
import ssl
import cookielib
import json
import sys
# from fuck12306_login import opener



### cookie 生成
c = cookielib.MozillaCookieJar()
c.load('cookie.txt', ignore_discard=True, ignore_expires=True)
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)

# 忽略证书认证
ssl._create_default_https_context = ssl._create_unverified_context

check_user = 'https://kyfw.12306.cn/otn/login/checkUser'
order_ticket = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
refer = 'https://kyfw.12306.cn/otn/leftTicket/init'


def add_header(req, url):
    # 对请求 添加 header
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    req.add_header('Referer', url)
    req.add_header('Host', 'kyfw.12306.cn')



req = urllib2.Request(order_ticket)
# data = {
#     '_json_att': ''
# }
data = {
    'secretStr': 'rbg8kDTTZO8TcRFcrn/6HFDFTNQhhV9iuiQbamUbHKg0GKJgbl2I5vCnVl9nKz/0jWJNlO5VcS0uRDTKxwRA0kZr6uYq5KewILynD+NfoMdjqU7IU+mE3MtrqDvvGBmGg0NsDQ/8xleae34fHtY7G/SEeMU4mRAb/1KRTLstzvPVsE/7tftaQHiOK1BvYJdFIuflwtBYuJyVdqdpZtH22PS7gx9XnJ0FDauBXjU51V81uEEtxu/KOw==',
    'train_date': '2017-12-05',
    'back_train_date': '2017-12-05',
    'tour_flag': 'dc',
    'purpose_codes': 'ADULT',
    'query_from_station_name': '北京',
    'query_to_station_name': '天津',
    'undefined': ''
}
data = urllib.urlencode(data)
print req, data
add_header(req, refer)


print req.headers
resault = opener.open(req, data=data)
print resault.read()