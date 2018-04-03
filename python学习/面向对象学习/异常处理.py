#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-30

__author__ = '@jiawenlong'
"""
try:
    # 代码块
    # i = int('1')
    i = input('请输入序号：')
    int(i)
except IndexError as e:
    print("\nIndexError", e, '\n')
except ValueError as e:
    print("\nValueError", e, '\n')
except Exception as e:
    # 上述代码如果出错，自动执行当前块
    # e 是 Exception的对象，对象中封装错误信息
    print("\nException", e)
else:
    # try 中没有报错执行try，如果有错就执行此处
    print("\nelse", i, '\n')
finally:
    # 不论上面是否报错，此处都执行
    print('finally', i)

# try:
#     raise Exception('主动触发异常')
# except Exception as e:
#     print(e)
"""

'''
def db():
    return False


def index():
    try:
        r = input('>>')
        int(r)
        
        
        resault = db()
        if not resault:
            r = open('log', 'a')
            r.write('连接失败')
            # raise Exception('连接失败')
    except Exception as e:
        str_error = str(e)
        print(str_error)

index()
'''

'''
# 自定义错误

class OldBoyError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


# obj = OldBoyError('xxx')
# print(obj)

try:
    raise OldBoyError('我错了。。。。')
except OldBoyError as e:
    print(e)
'''

# assert 条件 断言  用户用户服从，不服从就报错，并且可捕获，一般不捕获
# 条件必须满足，不满足就报错
print(123)
assert 1 == 2
print(567)
