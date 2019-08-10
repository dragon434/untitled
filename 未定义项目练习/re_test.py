#!/usr/bin/env python
#-*- coding:utf-8 -*-

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import os
import string


# pattern = re.compile(r'hello')
#
# match1 = pattern.match('hello world!')
# match2 = pattern.match('hellox world')
# match3 = pattern.match('helllo world')
#
# if match1:
#     print match1.group()
# else:
#     print 'Faile'
#
# if match2:
#     print match2.group()
# else:
#     print 'Faile'
#
# if match3:
#     print match3.group()
# else:
#     print 'Faile'
#
#
# ret = re.findall('f(as)', 'xdfreadfasas')
# print(ret)
# print(os.getcwd())

# striaaa = '((3+5*2/4)*3)*((2+7/3*5)-(4/2))'
# rent = re.findall('\([^()]+\)', striaaa)
# print 'source:', rent, striaaa

# ret = re.search('\([^()]+\)', striaaa)
# st = ret.group()
# print 'source:', st, striaaa

def addminus(s):
    ret = re.search('\d+\.?\d*[+-]\d+\.?\d*', s)
    if ret:
        ret = ret.group()
        x, y = re.split('[+-]', ret)
        x = float(x)
        y = float(y)
        ysf = re.search('[+-]', ret).group()
        if ysf == '+':
            resault = x + y
        else:
            resault = x - y
        resault = str(resault)
        end = s.replace(ret, resault)
        if re.search('-\d', end):
            # print '222', end
            return addminus(end)
        else:
            # print '1111', re.sub('[\(\)]', '', addminus(end))
            return re.sub('[\(\)]', '', addminus(end))
    else:
        return str(eval(s))


def chengchu(s):
    # global endend
    ret = re.search('\d+\.?\d*[*/]\d+\.?\d*', s)
    if ret:
        ret = ret.group()
        x, y = re.split('[*/]', ret)
        x = float(x)
        y = float(y)
        ysf = re.search('[*/]', ret).group()
        if ysf == '*':
            resault = x*y
        else:
            resault = x/y
        resault = str(resault)
        endend = s.replace(ret, resault)
        return chengchu(endend)
    else:
        return s


def check(s):
    ret = re.findall('([\(\)]+)', s)
    if ret:
        return 'True'
    if re.search('[*/]', s):
        ysf = re.search('[*/]', s).group()
        if ysf == '*':
            return '*'
        else:
            return '/'
    if re.search('[+-]', s):
        ysf = re.search('[+-]', s).group()
        if ysf == '+':
            return '+'
        else:
            return '-'


def js(s):
    if check(s) == 'True':
        rent = re.findall('\([^()]+\)', s)
        for i in rent:
            endrepl = chengchu(i)
            endall = addminus(endrepl)
            s = s.replace(i, endall)

        return addminus(s)
    elif check(s) == '*' or check(s) == '/':
        tmp = chengchu(s)
        if check(tmp) == '-' or check(tmp) == '+':
            return addminus(tmp)
        else:
            return tmp
    else:
        return addminus(s)


# striaaa = '(((3+2*4*10)*(5-2+3*4)+100-12*4/6+40-100)-(8*9/5-10+50/4)+(10-5+4*8/2-20+5.5))'
striaaa = '((1+2)*(3-5)-10)+5'
print "最终结果：", striaaa, '=', js(striaaa)

