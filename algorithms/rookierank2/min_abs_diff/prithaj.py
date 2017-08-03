#!/bin/python
import sys
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
a.sort()
min_diff = sys.maxint
for j in xrange(len(a)-1):
    min_diff = min(min_diff,abs(a[j]-a[j+1]))
print min_diff