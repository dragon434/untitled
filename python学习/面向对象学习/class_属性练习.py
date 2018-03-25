#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-03-22

__author__ = '@jiawenlong'

"""class 属性练习，实现分页效果"""

class create_page:
    def __init__(self, page):
        try:
            p = int(page)
            if p >= 11 or p <= 0:
                p = 1
        except Exception as e:
            p = 1

        self.page = p

    @property
    def start(self):
        current_page = (self.page - 1) * 10
        return current_page

    @property
    def end(self):
        current_page = self.page * 10
        return current_page

li = []
for i in range(1, 101):
    li.append(i)

while True:
    p = input("请输入想要查看的页码(1-10)->: ")
    page = create_page(p)
    print(li[page.start:page.end])

