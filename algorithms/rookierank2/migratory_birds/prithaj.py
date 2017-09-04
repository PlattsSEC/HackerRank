#!/bin/python
import sys
n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here
freq = {}
for i in types:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
max_freq,min_bird = max(freq.values()),sys.maxint
for j in freq:
    if freq[j] == max_freq:
        min_bird = min(min_bird,j)
print min_bird