#!/usr/bin/env python
# coding=utf-8
# author: yangrong
# date: 2015-8-19
# 本微信报警脚本应用于企业订阅号
# 当用户主动发消息给公众号的时候（包括发送信息、点击自定义菜单、订阅事件、扫描二维
# 码事件、支付成功事件、用户维权），微信将会把消息数据推送给开发者，开发者在一段时
# 间内（目前修改为48小时）可以调用客服消息接口，通过POST一个JSON数据包来发送
# 消息给普通用户，在48小时内不限制发送次数。



import os
import urllib2
import requests
import sys
import time
import json
import pickle

appid = 'wxc88**************'
secret = 'b9b8925aaa0eafc***********'
token_file = '/tmp/token_file.txt'
log_file = '/tmp/wechat.log'
openid_user_file = '/tmp/openid_user.txt'
openid_list = ["omPAFj8PBaE4UbdOGmgjFfq-shFM",  # 杨容
               "omPAFj27U-7PJkgYyHMk1wvDI27o",  # 阿飞
               ]  # 这是微信接收者的openid

# 报警格式，脚本名  收件人  标题  内容
# 这是zabbix发送内容格式，所以
# 这里取出标题和内容就行了

# 帮助信息,要求必须传参4个
if len(sys.argv) != 4:
    print 'Usage: %s mail-to title content' % sys.argv[0]
    print 'Example: '
    print '       %syangrong@jpush.cn  "this is testtitle"  "this is test content."' % sys.argv[0]
    sys.exit()

title = sys.argv[2]
content = sys.argv[3]
current_hour = time.strftime('%H', time.localtime(time.time()))


# 日志记录函数,把标题,用户id,状态记录
def log(title, openid, status):
    withopen(log_file, 'ab') as f:
    current_time = time.strftime('%Y-%m-%d%H:%M:%S', time.localtime(time.time()))
    f.write('%s| %s | %s | %s\n' % (current_time, openid, status, title))


# 获取token
class Token(object):
    def __init__(self, appid, secret):
        self.baseurl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(
            appid, secret)
        self.expire_time = sys.maxint

    def get_token(self):
        if self.expire_time > time.time():
            request = urllib2.Request(self.baseurl)
            response = urllib2.urlopen(request)
            ret = response.read().strip()
            ret = json.loads(ret)
            if 'errcode' in ret.keys():
                print >> ret['errmsg'], sys.stderr
                sys.exit(1)
            self.expire_time = time.time() + ret['expires_in']
            self.access_token = ret['access_token']
            token_pre = [current_hour, self.access_token]
            with open(token_file, 'wb') as f:
                pickle.dump(token_pre, f)

    return self.access_token


# access_token = Token(appid=appid,secret=secret).get_token()  #这是获取access_token的代码
# print access_token


# 获取所有的openid，然后根据openid获取用户信息，提取出用户名，最后输出用户名与openid的对应关系。
class get_user():
    def__init__(self):
    self.access_token = Token(appid, secret).get_token()


defget_openid_list(self):
openid_list_url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}&next_openid='.format(self.access_token)
request = urllib2.Request(openid_list_url)
response = urllib2.urlopen(request)
ret = response.read().strip()
openid_list = json.loads(ret)
# printopenid_list['data']['openid']
openid_list = openid_list['data']['openid']
foropenid in openid_list:
user_info_url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}'.format(self.access_token,
                                                                                                 openid)
user_info_request = urllib2.Request(user_info_url)
user_info_response = urllib2.urlopen(user_info_request).read().strip()
user_info = json.loads(user_info_response)
if 'errcode' in user_info.keys():
    print>> user_info['errmsg'], sys.stderr
    sys.exit()
withopen(openid_user_file, 'wb') as f:
f.write('openid:%s  nickname:%s' % (openid, user_info['nickname']))


# 使用post方式发送报警
def send_msg(title, content):
    # 一天能够获取的access_token次数是2000次，每次取到的token有效时间2小时，所以pickle dump时，把当前小时数与access_token写入文件，每一小时获取一次token.
    current_hour = time.strftime('%H', time.localtime(time.time()))
    ifnot
    os.path.exists(token_file):
    access_token = Token(appid, secret).get_token()


withopen(token_file, 'rb') as f:
token_pre = pickle.load(f)
# print'token_pre:',token_pre
access_token_pre = token_pre[1]
current_hour_pre = token_pre[0]
ifcurrent_hour == current_hour_pre:
access_token = access_token_pre
else:
access_token = Token(appid, secret).get_token()
# print'access_token:',access_token
# 循环openid_list，给每个成员单独推送微信消息
foropenid in openid_list:
# print'openid:',openid
url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s' % access_token
payload = {
    "touser": '%s' % openid,
    "msgtype": "text",
    "text": {
        "content": "Title: %s\nContent:%s" % (title, content)
    }
}
ret = requests.post(url, data=json.dumps(payload, ensure_ascii=False), verify=False)
result = ret.json()

# printresult
# 如果这一次发送失败,则代表可能access_token有问题,删除pickle dump文件,重新生成一次access_token
if result['errcode']:
    log(title, openid, 'sendfail')
    os.remove(token_file)
    access_token = Token(appid, secret).get_token()
else:
    log(title, openid, 'sendsuccess')

    # printpost(url, data)

# get_user().get_openid_list()   #这是遍历所有openid，获取openid和用户名的对应关系。

send_msg(title, content)  # 发送微信信息