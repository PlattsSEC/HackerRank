#!/bin/python

from collections import Counter

_ = input()
socks = Counter(raw_input().split())
print sum([socks[i]/2 if socks[i]%2==0 else (socks[i]-1)/2 for i in socks])