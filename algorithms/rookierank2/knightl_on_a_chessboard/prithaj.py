#!/bin/python
import sys
from collections import deque
def gen_nbrs(node,move,n):
    x,y = move[0],move[1]
    nbr = set()
    for i in [('+','-'),('-','+'),('-','-'),('+','+')]:
        a,b = node[0],node[1]
        if i[0] == '-' and i[1] == '+':
            a,b = a - x, b + y
        if i[0] == '+' and i[1] == '-':
            a,b = a + x, b - y
        if i[0] == '+' and i[1] == '+':
            a,b = a + x, b + y
        if i[0] == '-' and i[1] == '-':
            a,b = a - x, b - y
        if a >= 0 and a < n and b >= 0 and b < n:
            nbr.add((a,b))
    for i in [('+','-'),('-','+'),('-','-'),('+','+')]:
        a,b = node[0],node[1]
        if i[0] == '-' and i[1] == '+':
            a,b = a - y, b + x
        if i[0] == '+' and i[1] == '-':
            a,b = a + y, b - x
        if i[0] == '+' and i[1] == '+':
            a,b = a + y, b + x
        if i[0] == '-' and i[1] == '-':
            a,b = a - y, b - x
        if a >= 0 and a < n and b >= 0 and b < n:
            nbr.add((a,b))
    return nbr  

n = int(raw_input().strip())
moves, output = [(i,j) for i in xrange(1,n) for j in xrange(1,n)],[]

for i in moves:
    s,S,q,dist = (0,0),set(),deque(),{(k,j):-1 for k in xrange(n) for j in xrange(n)}
    dist[s] = 0
    S.add(s)
    q.append(s)
    while q:
        current_node = q.popleft()
        for j in gen_nbrs(current_node,i,n):
            if j in S: continue
            S.add(j)
            q.append(j)
            dist[j] = dist[current_node] + 1
    output.append(dist[(n-1,n-1)])

output,l = map(str,output),0
while l < len(output):
    print " ".join(output[l:l+n-1])
    l =l+n-1