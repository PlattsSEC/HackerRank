#!/bin/python
def return_weights(a):
    my_weights, prev, count = set(), '', 1
    for i in a:
        if i != prev:
            prev = i
            count = 1
        else:
            count +=1
        my_weights.add((ord(i)-96)*count)
    return my_weights
            
s = raw_input().strip()
n = input()
check = return_weights(s)
for _ in xrange(n):
    x = int(raw_input().strip())
    print("Yes" if x in check else "No")