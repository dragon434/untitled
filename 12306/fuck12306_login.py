#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : @jiawenlong

import urllib2
import urllib
import ssl
import cookielib
import json
import sys
from fuck12306_check_seat import check_seat


# 1 访问前需要login
# 2 请求前要其他操作
# 3 关联session ： 是否是相同的ip 操作  cookie 验证
#  12306 登陆过程
#     1. 请求登陆页面
#     2. 获取验证码
#     3. 请求验证码url做验证
#     4. 验证正确，请求登陆页面
#     5. 验证用户名密码，登陆
# 4 处理验证码
# 5 查询车票
# 6 预定车票
#       1 查询到车票后，验证用户，需要用到cookie或者session  https://kyfw.12306.cn/otn/login/checkUser
#       2 根据返回参数，为ture 预定车票：https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest

### cookie 生成
# c = cookielib.LWPCookieJar()
# cookie = urllib2.HTTPCookieProcessor()
# opener = urllib2.build_opener(cookie)

### cookie 保存到文件
cookiefile = 'cookie.txt'
c = cookielib.MozillaCookieJar(cookiefile)
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)

# 忽略证书认证
ssl._create_default_https_context = ssl._create_unverified_context

## 请求验证码，保存图片
# login 地址 带验证码的
codeimg_url = 'https://kyfw.12306.cn/otn/login/init'
#验证码图片地址
code_img = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.06510420729186484'
#校验验证码的地址
codeimg_request_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
# 真正的登陆地址
login_url = 'https://kyfw.12306.cn/passport/web/login'


def add_header(req, url):
    # 对请求 添加 header
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    req.add_header('Referer', url)


def receive_img():
    # 把 验证码 保存到当前目录 code.png
    req = urllib2.Request(code_img)
    add_header(req, codeimg_url)

    # 保存验证码图片
    codeimg = opener.open(req).read()
    with open('code.png', 'wb') as fn:
        fn.write(codeimg)


def input_codeimg():
    # 手动输入验证码坐标 如：248,105
    code = raw_input('[248,105,109,52,259,53]>>>>>>')
    # 验证验证码
    req = urllib2.Request(codeimg_request_url)
    data = {
        'answer': code,  # 验证码
        'login_site': 'E',
        'rand': 'sjrand'
    }
    # 把字典类型转换成查询字符串，post的字符串[a=1&b=2]
    data = urllib.urlencode(data)
    print "请求验证码的url的参数：", data
    add_header(req, codeimg_url)

    #需要带上cookie
    html = opener.open(req, data=data).read()
    # c.save(ignore_discard=True, ignore_expires=True)
    print "验证码验证后返回参数：", html
    return html


def login():
    req = urllib2.Request(login_url)
    add_header(req, codeimg_url)
    data = {
        'username': 'dragon434@sina.com',
        'password': '434wode434',
        'appid': 'otn'
    }
    data = urllib.urlencode(data)  # 把字典类型转换成查询字符串，post的字符串[a=1&b=2]
    print "请求登陆url的参数：", data

    html = opener.open(req, data=data).read()
    c.save(ignore_discard=True, ignore_expires=True)
    print "登陆请求验证返回参数：", html
    return html




print cookie,c
print opener
receive_img()
# print(html)
# #判断验证码是否验证成功
result = json.loads(input_codeimg())
if result['result_code'] == '4':
    print('验证码校验成功')
else:
    print('验证码校验失败')
    sys.exit()


# print(html)
# 判断验证码成功后，判断登陆是否成功
result = json.loads(login())
if result['result_code'] == 0:
    print('登录成功')
    c.save(ignore_discard=True, ignore_expires=True)
    print("查询是否有票")
    check_seat()
    print("有票，买票，点选验证码")
    print("没票，继续刷新")
else:
    print('登录失败')
    sys.exit()

