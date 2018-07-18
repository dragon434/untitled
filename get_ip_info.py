#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-07-02

__author__ = '@jiawenlong'

import requests
import os

#curl -s ipinfo.io/$(curl  -s http://ipv4.icanhazip.com )

def get_ip_info(ip):
        r = requests.get("http://ip.taobao.com//service/getIpInfo.php?ip=" + ip)
        info = r.json()["data"]
        # print(info)
        print("IP:", info["ip"])
        print("国家:", info["country"])
        print("省份:", info["region"])
        print("城市:", info["city"])
        print("供应商:", info['isp'])



get_ip_info(requests.get("http://ipv4.icanhazip.com").text.rstrip("\r\n"))
print()
get_ip_info("47.254.197.95")
get_ip_info("116.62.8.82")
# print()
# get_ip_info("8.8.8.8")
# print(requests.get("http://ipinfo.io/60.190.99.37").json())
# print(type(requests.get("http://ipv4.icanhazip.com").text))
