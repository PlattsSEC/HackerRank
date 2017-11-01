#!/bin/python
from operator import add,sub
from itertools import permutations as P
from collections import deque

def gen_board(a,b,n,moves):
    perms = list(P([a,b],2))
    return {(i,j):set([(m1(i,a),m2(j,b)) 
                       for a,b in perms 
                       for m1,m2 in moves if 0 <= m1(i,a) < n and 0 <= m2(j,b) < n])
                       for i in range(n) for j in range(n)
            }

def bfs(g,n):
    s,q,S = (0,0),deque(),set()
    dist = {k:-1 for k in g}
    dist[s] = 0
    S.add(s)
    q.append(s)
    while q:
        current_node = q.popleft()
        for i in g[current_node]:
            if i in S: continue
            q.append(i)
            S.add(i)
            dist[i] = dist[current_node] + 1
    return dist[(n-1,n-1)]


def main():
    n = input()
    moves = set(P([add,sub]*2,2))
    for i in range(1,n):
        x = []
        for j in range(1,n):
            x.append(bfs(gen_board(i,j,n,set(P([add,sub]*2,2))),n))
        print " ".join(map(str,x))

if __name__ == "__main__":
    main()