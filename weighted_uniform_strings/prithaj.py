#!/bin/python

import sys
import string

weights = {string.lowercase[i]:i+1 for i in xrange(len(string.lowercase))}

def return_weights(a):
    my_weights, prev, count = set(), '', 1
    for i in a:
        if i != prev:
            prev = i
            count = 1
        else:
            count +=1
        my_weights.add(weights[i]*count)
    return my_weights
            
s = raw_input().strip()
n = input()
check = return_weights(s)
for _ in xrange(n):
    x = int(raw_input().strip())
    if x in check:
        print "Yes"
    else:
        print "No"