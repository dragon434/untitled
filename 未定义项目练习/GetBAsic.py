#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getBASIC():
    loop = []
    while True:
        print("请输入参数：")
        S = input()
        if S.endswith('END'):
            loop.append(S)
            break
        else:
            loop.append(S)
    return loop


def findLine(prog, target):
    for i in range(0, len(prog)):
        if prog[i].startswith(target):
            return i


def execute(prog):
    location = 0
    args = []
    while True:
        if location == len(prog) - 1: return "success"
        T = prog[location].split()[0]
        location = findLine(prog, T)
        T = prog[location].split()[-1]
        location = findLine(prog, T)
        args.append('loop')
        if len(args) >= len(prog):
            return "infinite loop"


print(execute(getBASIC()))
# ("\n"
#  "10 GOTO 21\n"
#  "21 GOTO 37\n"
#  "37 GOTO 21\n"
#  "40 END\n"
#  "\n"
#  "5 GOTO 30\n"
#  "10 GOTO 20\n"
#  "20 GOTO 10\n"
#  "30 GOTO 40\n"
#  "40 END\n"
#  "\n"
#  "10 GOTO 20\n"
#  "20 END\n"
#  "\n"
#  "4 GOTO 12\n"
#  "12 GOTO 99\n"
#  "22 GOTO 22\n"
#  "99 GOTO 12\n"
#  "200 END\n"
#  "\n"
#  "10 GOTO 40\n"
#  "20 GOTO 25\n"
#  "25 GOTO 20\n"
#  "40 END\n")
