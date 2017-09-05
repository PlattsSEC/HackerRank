#!/bin/python

import sys


d1,m1,y1 = map(int,raw_input().strip().split(' '))
d2,m2,y2 = map(int,raw_input().strip().split(' '))
del_D,del_M,del_Y = d1-d2,m1-m2,y1-y2

if del_Y > 0:
    print 10000
elif del_M > 0 and del_Y == 0:
    print del_M * 500
elif del_D > 0 and del_M == 0 and del_Y == 0:
    print del_D * 15
else:
    print 0