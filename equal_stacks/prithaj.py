#!/bin/python

import sys

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
h1.reverse()
h2.reverse()
h3.reverse()
s1,s2,s3 = [],[],[]
sum1,sum2,sum3 = 0,0,0
for i in range(len(h1)):
    sum1 = sum1 + h1[i]
    s1.append(sum1)
s1.reverse()
for i in range(len(h2)):
    sum2 = sum2 + h2[i]
    s2.append(sum2)
s2.reverse()
for i in range(len(h3)):
    sum3 = sum3 + h3[i]
    s3.append(sum3)
s3.reverse()

# Figure out which one is the smallest list and iterate through it
if len(s1)<len(s2) and len(s1)<len(s3):
    for i in s1:
        if i in s2 and i in s3:
            print i
            break
    else:      
        print 0
elif len(s2)<len(s1) and len(s2)<len(s3):
    for i in s2:
        if i in s1 and i in s3:
            print i
            break
    else:
        print 0
elif len(s3)<len(s2) and len(s3)<len(s1):
    for i in s3:
        if i in s1 and i in s2:
            print i
            break
    else:
        print 0
elif len(s1)==len(s2)==len(s3):
    for i in s1:
        if i in s2 and i in s3:
            print i
            break
    else:
        print 0