#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2017-12-26

__author__ = '@jiawenlong'

import re

big = {
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖',
    '0': '零'
}
dw = {
    -1: '',
    0: '',
    1: '',
    2: '拾',
    3: '佰',
    4: '仟',
    5: '万',
    6: '拾',
    7: '佰',
    8: '仟',
    9: '亿'
}
xs = {
    0: '',
    1: '角',
    2: '分',
    3: '里',
    4: ''
}


def zhongwen(s):
    end = ''
    if re.findall('\.', s):
        z, f = s.split('.')
        wei = len(z)
        for i in z:
            if i == '0':
                end = end + ''
            else:
                end = end + big[i] + dw[wei]
            wei -= 1

        if len(f) >= 4:
            f = f[0:3]
            wei = 1
        else:
            wei = 1

        for i in f:
            end = end + big[i] + xs[wei]
            wei += 1
        print(end)
    else:
        wei = len(s)
        for i in s:
            if i == '0':
                end = end + ''
            else:
                end = end + big[i] + dw[wei]
            wei -= 1
        end = end + "圆整"
        print(end)


if __name__ == '__main__':
    num = input('请输入要转换的数字_>：')
    if num:
        zhongwen(num)
    else:
        print("请输入数字！！")
