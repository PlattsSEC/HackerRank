#!/bin/python

import sys
from collections import Counter

_ = int(raw_input().strip())
freq = Counter(map(int,raw_input().strip().split(' ')))
new_arr = freq.keys()
new_arr.sort()
max_num = freq.most_common(1)[0][1]
for i in xrange(len(new_arr)-1):   
    x,y = new_arr[i],new_arr[i+1]
    if abs(x-y)<=1:
        max_num = max(max_num,freq[x]+freq[y])
print max_num