#!/bin/python

import sys
from collections import Counter

s = raw_input().strip()
n = long(raw_input().strip())

a_count = Counter(s)["a"]
n_1 = a_count*(n/len(s))
n_2 = sum([1 for i in range(n%len(s)) if s[i] == "a"])
print n_1+n_2