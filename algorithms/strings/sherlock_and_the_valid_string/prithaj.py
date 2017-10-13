#!/bin/python
from collections import Counter
import sys

def is_valid(s):
    if len(set(Counter(s).values())) == 1:
        return True
    else:
        return False

s = raw_input().strip()
freq = Counter(s)
if is_valid(s):
    print "YES"
else:
    for i in set(s):
        if is_valid(s.replace(i,"",1)):
            print "YES"
            break
    else:
        print "NO"