#!/usr/bin/python

T = input()
for _ in range(T):
    x = list(raw_input())
    suffix = [] 
    
    for j in x[::-1]: 
        if suffix:
            if suffix[-1] <= j:
                suffix.append(j)
            else:
                break
        else:
            suffix.append(j)
    
    suffix = suffix[::-1]
    prefix = x[:len(x)-len(suffix)]

    if prefix:
        for k in range(len(suffix)):
            if suffix[-k-1] > prefix[-1]:
                prefix_succ = -k-1
                break

        prefix[-1], suffix[prefix_succ] = suffix[prefix_succ], prefix[-1]
        suffix = suffix[::-1]
        print "".join(prefix+suffix)
        
    else:
        print "no answer"