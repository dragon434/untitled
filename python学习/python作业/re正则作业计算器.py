#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/11/14 22:11

__author__ = 'JiaWenLong'

import re


# 运算符  未完成
# print(re.search('-?\d+\.?\d{0,}(?P<operator>[+_*/])-?\d+\.?\d{0,}', inter_js).group('operator'))
# print(isinstance(-40, int))
# print(isinstance(5.0, float))


# 定义相关函数
def is_float(n):
    try:
        return float(re.search('-?\d+\.\d+', n).group())
    except AttributeError:
        return False


def is_int(n):
    try:
        if is_float(n):
            return is_float(n)
        else:
            return int(re.search('-?\d+', n).group())
    except AttributeError:
        return False


def muti_div(s):
    operation = re.compile('(?P<front>\d+\.?\d*)(?P<operators>[*/])(?P<behind>-?\d+\.?\d*)')
    res = s
    i = 0
    while i < len(re.findall('[*/]', s)):
        # print('muti_div ', res)
        opt = operation.search(res).group('operators')
        a = is_int(operation.search(res).group('front'))
        b = is_int(operation.search(res).group('behind'))
        expre_ssion = operation.search(res).group()

        # print('mut_div_Front_Behind_():', a, b)
        if opt == '*':
            result = a * b
            res = res.replace(expre_ssion, str(result))
            # print('*', res)
            # return muti_result
        else:
            # if isinstance(a, float) or isinstance(b, float):
            result = a / b
            res = res.replace(expre_ssion, str(result))
                # print('/', res)
                # return div_result
            # else:
            #     result = a // b
            #     res = res.replace(expre_ssion, str(result))
            #     # print('//', res)
            #     # return div_result
        i += 1
        # print('final', res)
        # print('='*50)
    return res


def add_minus(s):
    operation = re.compile('(?P<front>-?\d+\.?\d*)(?P<operators>[+-])(?P<behind>\d+\.?\d*)')
    s = format_strings(s)
    res = s
    # print('add_minux: ', res)

    try:
        operation.search(res).group('operators')
    except :
        return res

    i = 0
    if re.search('\(-', s) or re.search('^-', s):
        j = len(re.findall('[+-]', s)) - 1
    else:
        j = len(re.findall('[+-]', s))

    while i < j:
        opt = operation.search(res).group('operators')
        a = is_int(operation.search(res).group('front'))
        b = is_int(operation.search(res).group('behind'))
        expre_ssion = operation.search(res).group()

        # print('add_minus_Front_Behind_():', a, b, s)
        if opt == '+':
            result = a + b
            res = res.replace(expre_ssion, str(result))
        else:
            result = a - b
            res = res.replace(expre_ssion, str(result))

        i += 1
        # print(res)
    return res


def format_strings(s):
    string = s.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('--', '+')
    string = string.replace('-+', '-')
    string = string.replace(' ', '')
    return string

s1 = '1-2*((60-30+(9-2*5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)*(-40/5+6))'
s2 = '1 - 2 * ((60-30 + (-40/(-5)) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*-3)/(16-3*2))'
s = '1 - 2 * ((60-30 + (40/-5) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(4*(-3))/(16-3*2))'

print('eval:', eval(s))
while re.search('\(', s):

    # print('yuan: ', s)
    s = format_strings(s)
    brackets = re.compile('\([^()]+\)')
    expressions = brackets.findall(s)
    mv_brackets = re.compile('\(([-+]?\d+.?\d*)\)')

    # print('=' * 30)
    for expression in expressions:
        # print('E: ', expression)
        # expression = brackets.search(s).group()
        resault = muti_div(expression)
        finalyt = add_minus(resault)
        s = s.replace(expression, finalyt)
        # print('R', s)
        s = mv_brackets.sub(r'\1', s)
        # print('mv_brackets: ', s)
        s = format_strings(s)
        # print('format: ', s)
else:
    resault = muti_div(s)
    # print(resault)
    finalyt = add_minus(resault)
    # print(finalyt)
    s = s.replace(s, finalyt)
print('Finally: ', s)

# 关键在于 r
# bold = re.compile(r'\*{2}(.*?)\*{2}')
# text = 'Make this **cai**. This **junsheng**.'
# print('Text:', text)
# print('Bold:', bold.sub(r'<b>\1</b>', text))

# strings = s
# while re.search('\(', strings):
#     expression = brackets.search(s).group()
#     resault = muti_div(expression)
#     finalyt = add_minus(resault)
#     strings = strings.replace(expression, finalyt)
#     print('R', strings.replace(expression, finalyt))
#     #     print('='*30)
# else:
#     muti_div(strings)
#     add_minus(strings)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # 获取所有括号和内部的表达式
# brackets = re.compile('\([^()]+\)')
# inter_brackets = brackets.findall(s)
# print('inter_brackets', inter_brackets)
# # 运算符判断
# ope = re.compile('\d+\.?\d{0,}(?P<operators>[+\-*/])\d+\.?\d{0,}')
# # operator = ope.search(inter_brackets[0]).group('operators')
# # print(operator)
# print('inter_brackets[0]', inter_brackets[0])
#
# # 浮点数 或者 整数 匹配
# flaodORint = re.findall('-?\d+\.?\d{0,}', inter_brackets[0])
# print('flaodORint :', flaodORint)
#
# for i in range(0, len(flaodORint)):
#     NEXT = i+1
#     # print(NEXT)
#     if NEXT < len(flaodORint):
#         print(flaodORint[i], flaodORint[NEXT])
#         operator = ope.search(inter_brackets[0]).group('operators')
#         if operator == '+' or operator == '-':
#             value = add_minus('9-2*5')
#         if operator == '*' or operator == '/':
#             value = muti_div('9-2.7*5')
#
# print(value)
# ret = muti_div('9-2.7*5')
# print('ret', ret)
# print(add_minus('9-2.8*5'))


# #######################################################
# s = '1 - 2 * ((60-30 + (5-40/5) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# s1 = '1 - 2 * ((60-30 + (-40/(-5)) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*(-3))/(16-3*2))'
# s2 = '1 - 2 * ((60-30 + (40/-5) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(4*(-3))/(16-3*2))'
#
# inter_kh = re.search('\([^()]+\)', s).group()
# inter_js = re.sub('[()]', '', inter_kh)
# print(inter_js, inter_kh)
# ope = re.compile('\d+\.?\d{0,}(?P<operators>[+\-*/])\d+\.?\d{0,}')
# operator = ope.search(inter_js).group('operators')
# print(operator)
#
# # 浮点数 或者整数匹配
# l_n = re.findall('-?\d+\.?\d{0,}', inter_js)
# print('l_n :', l_n)
#
#

#

#
#
# # print(is_int(l_n[0]) / is_int(l_n[1]))
# print(value)
# print(re.sub('-8+5', str(value), s))
