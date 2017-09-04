#!/bin/python

import sys

_,_ = raw_input().split()

A = map(int, raw_input().split())
B = map(int, raw_input().split())

max_A, min_B, count = max(A),min(B), 0
for x in range(max_A, min_B+1):
    A_0 = filter(lambda a:x%a==0, A)
    B_0 = filter(lambda b:b%x==0, B)
    if A_0==A and B_0==B:
        count += 1    
print count