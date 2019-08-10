#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import urllib2
import re
page=1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    cotent = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author.*?>.*?<a.*?<img.*?>.*?</a><a.*?<h2>(.*?)</h2>.*?<div.*?<span>(.*?)</span>.*?</div>.*?</div>.*?<span>.*?<i.*?>(.*?)</i>.*?<a.*?<i>(.*?)</i>',re.S)
    print pattern
    items = re.findall(pattern,cotent)
    print items
    for item in items:
        print item[0],item[1],item[2],item[3]
    print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
