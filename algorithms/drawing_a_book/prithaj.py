#!/bin/python

import sys

n = input()
p = input()
# your code goes here
front,back,f_n,b_n = [0,1],[n-1,n],0,0
while True:
    if p in front:
        break
    
    front[0] = front[1]+1
    front[1] = front[1]+2
    f_n +=1
    
while True:
    if p in back:
        break
    
    back[0] = back[1]-3
    back[1] = back[1]-2
    b_n +=1
    
print min(f_n,b_n)