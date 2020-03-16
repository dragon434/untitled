#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/11/4 21:05

__author__ = 'JiaWenLong'

import re

# findall 取出全部匹配到的字符
# findall 第一个参数是规则，第二个参数是匹配的字符串。2个参数都必须是字符串
print(re.findall('w*', 'hell world'))
print(re.findall('a[a,d ,c]', 'ad x'))
print(re.findall('[^4,5]', 'iu124i5,'))
print(re.findall('[^45]', 'iu124i5,'))
print(re.findall('u.n', r'iu\n124i5,'))
print(re.findall('u.n', 'iu\n124i5,'))

print('反斜杠的意义')
# \d 匹配是兼职数字，任意一个
# \D 匹配任意非数字
# \s 匹配任意空白字符
# \S 匹配任意非空白字符
# \w 匹配任意字母数字字符
# \W 匹配任意非字母数字字符
# \b 匹配一个单词边界，即单词和空格的位置
print(re.findall('\d', 'iu124i5,'))
print(re.findall('\d{2}', 'iu124i567,'))
print(re.findall('\d{2,3}', 'iu124i567,'))
print(re.findall('\D', 'iu12\s4i\n5$67,'))
print(re.findall('\s', 'iu 12%4i\t5$67,'))
print(re.findall('\S', 'iu 12  4i \t567,'))
print(re.findall('w\w{2}l', 'hell wo0ld'))
print(re.findall('\W', 'hell w$o0%l\d!@#$&*(\p'))
print(re.findall(r'l\b', 'hell&wo0l$d'))

####################
print('re.search 匹配到第一个后结束')
print(re.search('[1-9]+', 'iu123abcheloword1234').group())
print(re.search(r"\\p", 'iu123abcheloword1234\p').group())
print(re.search("\.", 'iu123abcheloword.123.4\p').group())

print('反斜杠的转译')
print(re.findall("\\\\", "abc\ed"))
print(re.findall(r"\\", "abc\ed"))
print(re.findall(r"\bbelo", "belo"))
print(re.findall("\\bbelo", "belo"))

# 分组 + [1,OO)| ? [0,1]
print('分组')
print(re.search('(as)+', 'adasfdks').group())
print(re.findall('(as)?', 'adafaadksa'))
print(re.findall('(as)+', 'adafaasdkasa'))

# 通过组名取字段 格式 (?P<组名>正则)
ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})', 'wer34ttt098/ooo')
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))

print('match 只在字符串开始匹配,返回开头的第一个匹配到的对象')
print(re.match('asd', 'adfgasd'))
print(re.match('asd', 'asdfgasd').group())

# 中括号中所有字符都是或者关系
print('字符分割 split, 第一个参数是分割关键字，第二个为被分割的字符串')
print(re.split('[@:]', '3@15:09:35'))
print(re.split('[\.3@]', '3@15:09:35.789'))
print(re.split('[ks]', 'lsk,-salk'))
print(re.split('[k,s]', 'lsk,-salk'))


# sub 替换 第一参数是 正则匹配，第二个是要替换的字符串，第三个是被替换的字符串
print('sub 匹配替换，类似sed')
print(re.sub('a..x', 'sxxxb', 'hfjasalexxdhf'))

# 编译
print('compile 编译匹配')
print(re.compile('\.com'))
obj = re.compile('\.com')
print(obj.findall('sdjfsldfj.comwoehrow'))
print(obj.split('sdfg.comwertyu'))
print(obj.sub('.cn', 'www.baidu.com'))

test = re.compile('\([^()]+\)')
print(test.findall('1 - 2 * ((60-30 + (-40/5) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'))