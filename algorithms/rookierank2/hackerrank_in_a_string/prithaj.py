#!/bin/python

import sys
word = "hackerrank"
q = int(raw_input().strip())
for a0 in xrange(q):
    s = list(raw_input().strip())
    # your code goes here
    i = 0
    while i<len(word):
        if s[i] == word[i]:
            i +=1
        else:
            del s[i]
        if len(s) < len(word):
            break
    if word in "".join(s):
        print "YES"
    else:
        print "NO"