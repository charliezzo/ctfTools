# -*- coding:utf8 -*-
# 使用windows系统

from random import *

def mix():
    mixed_flag='WHWEV3JRPQYFV22ZY8KUSM0SR0AdgEhupcni9355074983089834650'
    seed("www.ChaMd5.org")
    out=''
    # assert randrange(0,100)==78
    for c in mixed_flag:
        if c.islower():
            out+= chr((ord(c)-0x61+randrange(0,26))%26 + 0x61)
        elif c.isupper():
            out+= chr((ord(c)-0x41+randrange(0,26))%26 + 0x41)
        elif c.isdigit():
            out+= chr((ord(c)-0x30+randrange(0,10))%10 + 0x30)
        else:
            out+= c
    print out
    #输出是 SACBK8AEJCAOW52YL9ANBO7PQ0YvrEajcxnu7784704595388694801

    pass

if __name__ == '__main__':
    mix()