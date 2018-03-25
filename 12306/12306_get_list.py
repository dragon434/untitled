#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : @jiawenlong

import urllib2
import ssl
from json import loads
import sys
from func_12306_get_city import get_city_code  # 查询城市信息，返回城市代码

ssl._create_default_https_context = ssl._create_unverified_context  # 忽略证书认证

# start_station = sys.argv[1]
# ended_station = sys.argv[2]
# train_date = sys.argv[3]
# train_name = sys.argv[4]

start_station = raw_input('请输入始发站：')
ended_station = raw_input('请输入终点站：')
train_date = raw_input('请输入乘车日期：')
train_name = raw_input('请输入车次或者不输入：')
from_station = get_city_code(start_station)
to_station = get_city_code(ended_station)
if train_name:
    train_name = train_name.upper()

# print train_name
# train_date = '2017-12-01'
# train_name = 'K261'
# train_date = '2017-11-25'

# 城市 https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9027
# 请求的 火车票  的地址 包含了 始发站 目的站 乘车时间
ticket = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + train_date + \
         '&leftTicketDTO.from_station=' + from_station + \
         '&leftTicketDTO.to_station=' + to_station + \
         '&purpose_codes=ADULT'


def getSeat():
    html = urllib2.urlopen(ticket).read()
    dict = loads(html)
    # print dict['messages'][0]
    if dict['messages']:
        print dict['messages'][0]
        sys.exit()
    else:
        return dict['data']['result']


def get_train(**kwargs):
    trains = kwargs
    return trains


def check_seat():
    """暂时只打印一个车次的 我们需要的 信息"""
    for i in getSeat():
        split_list = i.split('|')
        train = get_train(ticket_name=split_list[3], start_time=split_list[8], end_time=split_list[9],
                          live_time=split_list[10],
                          soft_sleeper=split_list[23], no_seat=split_list[26], hard_sleeper=split_list[28],
                          hard_seat=split_list[29], second=split_list[30], first=split_list[31], buss=split_list[32])
        # print train['soft_sleeper']
        if train_name and train_name == train['ticket_name']:
            print train['ticket_name']
        else:
            print train['ticket_name']
        # break

check_seat()

# def getSeat():
#     # print my_ticket
#     html = urllib2.urlopen(ticket).read()
#     # print(html)
#     # print(type(html))
#     # print(loads(html))
#     dict = loads(html)
#     # print dict['data']['result']
#     # print dict
#     return dict['data']['result']
#
# def print_seat():
#     """暂时只打印一个车次的 我们需要的 信息"""
#     train = {}
#     for i in getSeat():
#         split_list = i.split('|')
#         train = get_train(ticket_name=split_list[3], start_time=split_list[8], end_time=split_list[9], live_time=split_list[10], \
#                   soft_sleeper=split_list[23], no_seat=split_list[26], hard_sleeper=split_list[28], \
#                   hard_seat=split_list[29], second=split_list[30], first=split_list[31], buss=split_list[32])
#
#         # train['ticket_name'] = split_list[3]
#         # train['start_time'] = split_list[8]
#         # train['end_time'] = split_list[9]
#         # train['live_time'] = split_list[10]
#         # train['soft_sleeper'] = split_list[23]
#         # train['no_seat'] = split_list[26]
#         # train['hard_sleeper'] = split_list[28]
#         # train['hard_seat'] = split_list[29]
#         # train['second'] = split_list[30]
#         # train['first'] = split_list[31]
#         # train['buss'] = split_list[32]
#         # for key in train:
#         #     print key, train[key]
#         # yield train
#
#         # print "车次:", split_list[3],
#         # print "\t开车时间:", split_list[8],
#         # print "\t到站时间:", split_list[9],
#         # print "\t历时时间:", split_list[10],
#         # print "\t软卧:", split_list[23],
#         # print "\t无座:", split_list[26],
#         # print "\t硬卧:", split_list[28],
#         # print "\t硬座:", split_list[29],
#         # print "\t二等座:", split_list[30],
#         # print "\t一等座:", split_list[31],
#         # print "\t商务座:", split_list[32]
#
#         # break
#

# getList()
# [1] 预订
# [2] 240000K4730C
# [3] K473          车次
# [4] BJP
# [5] KMM
# [6] BJP
# [7] BFF
# [8] 16:16         开车时间
# [9] 05:57         到站时间
# [10] 13:41        经过时间
# [11] Y
# [12] ZiGu2UrItHRf0TWQL%2Fpgp35uRTKLjh%2BfVFvsFlM1cUCXe2Knv5CIDrPScyk%3D
# [13] 20171124
# [14] 3
# [15] PA
# [16] 01
# [17] 14
# [18] 0
# [19] 0
# [20]
# [21]
# [22]
# [23] 无            软卧
# [24]
# [25]
# [26] 有            无座
# [27]
# [28] 无            硬卧
# [29] 无            硬座
# [30]               二等座
# [31]               一等座
# [32]               商务座
# [33]
# [34] 10401030
# [35] 1413
