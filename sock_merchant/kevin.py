#!/bin/python3
# Kevin Boyette
import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

counts = []
counter = 0
for i in c:
    if i in counts:
        counter += 1
        counts.remove(i)
    else:
        counts.append(i)

print(counter)
