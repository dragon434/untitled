#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-06-15

import json

json_info = '/Users/admin/Documents/crt/json.log'
log = open(json_info, 'rb')
end = open('/Users/admin/Documents/crt/end.txt', 'w+')

# 读取每一行
for line in log.readlines():
    # 转换json 为字典
    json_s = json.loads(line)
    for k in json_s:
        if k == 'plain':
            Dict = json_s['plain']
            # print(Dict)
            # print(json.dumps(Dict, ensure_ascii=False))
            # ensure_ascii=False dumps 默认是使用ascii 对中文进行编码，这个参数禁止使用ascii对中文进行编码
    # 判断 字典 中是否 包含key值 payStatus
    if 'payStatus' in Dict.keys():
        Upay = "(F" + "'" + Dict["outTradeNo"] + "'" + "," + "'" + Dict["errCodeDes"] + "'" + "," + "'" + \
              Dict['payStatus'] + "'" + ")" + ","
        # print(Upay)
        end.write(Upay)
        end.write('\n')
        # print("(F" + "'" + Dict["outTradeNo"] + "'" + "," + "'" + Dict["errCodeDes"] + "'" + "," + "'" + \
        #       Dict['payStatus'] + "'" + ")" + ",")

    else:
        Upay = "(S" + "'" + Dict["outTradeNo"] + "'" + "," + "'" + Dict["errCodeDes"] \
              + "'" + "," + "'" + "'" + ")" + ","
        # print(Upay)
        end.write(Upay)
        end.write('\n')
        # print("(S" + "'" + Dict["outTradeNo"] + "'" + "," + "'" + Dict["errCodeDes"] \
        #       + "'" + "," + "'" + "'" + ")" + ",")

# i = "xxx"
# i.encode('utf-8')
