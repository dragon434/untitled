#!/usr/bin/env python
#-*- coding:utf-8 -*-



### 查找给出的目录中 所有 txt 结尾的文件
#path = raw_input("请输入目录路径——>: ")
#print(os.getcwd())  ### 当前目录
#os.chdir(path)      ### 转换目录
#print(os.getcwd())


# find 1
#path = "/Users/admin/Downloads"
#keys = "txt"
#files = os.walk(path) # 遍历所有目录 files 是个地址
#for file in files: # file 是 给出路径下的所有目录以及目录下的文件，是一个元组 file 是 eg: ('/Users/admin/Downloads/apk/\xe5\x95\x86\xe6\x88\xb7app', [], ['bqboss_2.8.6.apk', 'bqboss_2.8.7.apk', 'bqboss_2.8.8.apk', 'bqboss_2.8.9.apk'])
#    for i in file:  #  i 是一个列表 根据file来遍历
#        for k in i:  # k 是文件名，或者目录名 根据 file i 来遍历
#            if k.endswith(keys):   # k 是文件名
#                print file[0] + "/" + k  # 输出给出的路径和文具吗

#one
#path = "/Users/admin/Downloads"
#keys = "txt"
#for parent, dirname, filenames in os.walk(path):
#    for filename in filenames:
#        if filename.endswith(keys):
#            print parent + "/" + filename

# find 2
#def findfile(inputdir):
#    txtlist = []
#    for parent, dirnames, filename in os.walk(inputdir):
#        #print parent,dirnames
#         for filenames in filename:
#             txtlist.append(filenames)
#     return fnmatch.filter(txtlist, '*.txt')  ## fnmatch.filter()第一个参数必须是列表
# findfile(path)
# #print(findfile(path))

## 竖排文字  行转列
# x = u"静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡."
# k = 0
# for i in range(0,6): #行
#     s = ""
#     for m in range(0,5): # 列
#         s += x[ i + 6 * m ] + "|"
#         k += 1
#         if k%5 == 0: print s ;continue

# import os
# import fnmatch
# ### python 实现grep -lr
# search="微信"
# path = "/Users/admin/Downloads/crt"
# keys = "txt"
# for parent, dirname, filenames in os.walk(path):
#     for filename in filenames:
#             file = parent + "/" + filename
#             f = open(file,'r')
#             print file
#             while True:
#                 line = f.readline()
#                 if search in line:
#                     print file
#                     f.closed
#                     break
            # print parent + "/" + filename



import pandas as pd
import codecs

# xd = pd.ExcelFile('/Users/admin/Documents/work/日报-周报/运维日报(2017-09-15-贾文龙).xlsx')
# df = xd.parse(xd.sheet_names, header=None, keep_default_na=True)
# df = pd.read_excel('/Users/admin/Documents/work/日报-周报/运维日报(2017-09-15-贾文龙).xlsx', sheetname=0)
# print df.dtypes

# with codecs.open("/Users/admin/Documents/work/日报-周报/0915.html", "w", "utf-8") as rb:
#     rb.write(df.to_html(header=False, index=False,))

#
# import xlrd
# import datetime as dt
# import os
#
# DT=dt.date.today().strftime('%Y-%m-%d')
# file_name="/Users/admin/Documents/work/日报-周报/运维日报(" + DT + "-贾文龙).xlsx"
# md_file="/Users/admin/Documents/work/shells/rb.md"
#
# rb=open(md_file,'w')
# book = xlrd.open_workbook(file_name)
# print "The number of worksheets is", book.nsheets
# # print "Worksheet name(s):", book.sheet_names()[0]
# sh = book.sheet_by_index(0)
# # print sh.name, sh.nrows, sh.ncols
#
# for hang in range(0, sh.nrows):
#     if hang == 0 or hang == 1:
#         continue
#     for lie in range(0, sh.ncols):
#         if sh.cell_value(rowx=hang, colx=lie):
#             value = sh.cell_value(hang, lie)
#         if lie == 5:
#             print "|"
#             rb.write("|" + '\n')
#             if hang == 2 and lie == 5:
#                 print  "|--|--|--|--|--|"
#                 rb.write("|--|--|--|--|--|" + '\n')
#         else :
#             print "|",
#             rb.write("|")
#             # print("\t%-30s") % value.encode("utf-8"),
#             print("%s") % value.encode("utf-8"),
#             rb.write(value.encode("utf-8"))
# rb.closed


                # print h, l
# for rx in range(sh.nrows):
#     # print sh.row(rx)
#     h = sh.row(rx)
#     for i in h:
#         print i.dump(, header=False)


# st = book.sheet_by_index(0)
# print book.sheet_by_name(u'技术日报')
# print book.sheet_names()
# print book.sheet_names()[0]
# print st.name, st.nrows, st.ncols


# ##### 温度转换
# def F2C(f):
#     C = (f - 32) * (5.0/9)
#     return str(C) + "C"
# def C2F(c):
#     F = c * (9.0/5) + 32
#     return str(F) + "F"
#
# W = raw_input("请输入温度：")
# if W.endswith("C"):
#     W = float(W.replace("C", ""))
#     print(float(W),type(W))
#     print(C2F(W))
# elif W.endswith("F"):
#     W = float(W.replace("F", ""))
#     print(float(W),type(W))
#     print(F2C(W))

# #### 信用检查
# def add(S):
#     sumh = 0
#     S = S.replace(" ", "")
#     for i in S:
#         sumh += int(i)
#     return sumh
#
# def if_ok(str_list):
#     for string in str_list:
#         if len(string) == 4 and len(str_list) == 4 and string.isdigit():
#             if_or_not = True
#         else:
#             if_or_not = False
#     return if_or_not
#
# def check(S):
#     if S.startswith(" ") or S.endswith(" ") or S == "":
#         # return False
#         print("卡号输入错误！请重试！")
#     L = S.lstrip().split()
#     if if_ok(L) :
#         resault = add(S)
#         if resault%10 == 0:
#             print("您的卡号为： %s" % S)
#             # return True
#         else:
#             # return False
#             print("卡号输入错误！请检查！")
#     else:
#         # return False
#         print("卡号输入错误！请检查！")
#
# # print(check('9384 3495 3297 0121'))
# check('9384 3495 3297 0121')
# check('0000000000000000')


# ####
# l = [1,2,3,4,4,3,0,4]
#
# def max_num(n):
#     a = n
#     b = 0
#     if a > b:
#         max = a
#     return max
#
# max_num(1)
# for i in l:
#     print l.count(i)
#     # print max(l.count(i))



#
# def outer():
#     x=100
#     def inner():
#         x+=100
#         print(x)
#     return inner
#
#
# myx=outer()
# myx()


import requests
import json

ZABIX_ROOT = 'http://zabbix.bqmart.cn/api_jsonrpc.php'
url = ZABIX_ROOT + '/api_jsonrpc.php'

# user.login
payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        'user': 'admin',
        'password': 'zabbix',
    },
    "auth": None,
    "id": 0,
}
headers = {
    'content-type': 'application/json',
}
req = requests.post(url, json=payload, headers=headers)
auth = req.json()
print 'req:', req
print 'auth:', auth

# host.get
payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        'output': [
            'hostid',
            'name'],
    },
    "auth": auth['result'],
    "id": 2,
}
res2 = requests.post(url, data=json.dumps(payload), headers=headers)
res2 = res2.json()
print 'res2:', res2

for host in res2['result']:
    print host['name']







