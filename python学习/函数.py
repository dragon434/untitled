#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2019/7/8 22:19


def logger(log_text):
    f = open("log.txt", 'a')
    f.write(log_text)
    f.close()
    print(log_text)

logger('Hello')
# subroutine 【子程序】 , procedures 【过程】   函数
# 作用： 减少重复代码、方便修改、更易扩展、保持代码一致性
