#!/bin/python
from itertools import combinations

def check_if_t(s):
    chars = list(set(s))
    return True if s == "".join([chars[i%2] for i in range(len(s))]) or s == "".join([chars[::-1][i%2] for i in range(len(s))]) else False

n = input()
s = raw_input()
chars = combinations(set(s),2)
try:
    print max(map(len,filter(check_if_t,["".join([j for j in s if j == k[0] or j == k[1]]) for k in chars])))
except:
    print 0
