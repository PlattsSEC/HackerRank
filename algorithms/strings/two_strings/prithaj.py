#!/bin/python
from itertools import combinations

def check_if_t(s):
    chars = list(set(s))
    flag = False
    if s == "".join([chars[i%len(chars)] for i in range(len(s))]) or s == "".join([chars[::-1][i%len(chars)] for i in range(len(s))]):
        flag = True
    return flag

n = input()
s = raw_input()
chars = combinations(set(s),2)
try:
    print max(map(len,filter(check_if_t,["".join([j for j in s if j == k[0] or j == k[1]]) for k in chars])))
except:
    print 0