#!/bin/python
n = input()
for i in range(n):
    x = raw_input()
    new_str, ref, count = [], "hackerrank",0
    for j in x:
        try:
            if j == ref[count]:
                new_str.append(j)
                count += 1
        except:
            break
    if "".join(new_str) == ref:
        print "YES"
    else:
        print "NO"