#!/bin/python

import sys

def generate_neighbors(t,g):
    i,j = t
    nghbrs = []
    for x,y in ((i-1,j-1),
                (i-1,j),
                (i-1,j+1),
                (i,j-1),
                (i,j+1),
                (i+1,j-1),
                (i+1,j),
                (i+1,j+1)):
        try:
            if x>=0 and y>=0 and g[x][y] == "1":
                nghbrs.append((x,y))
        except:
            continue
    return nghbrs

def dfs(g,s,S=set(),dfs_sum=0):
    S.add(s)
    dfs_sum+=1
    for i in generate_neighbors(s,g):
        if i in S: continue
        dfs_sum = dfs(g,i,S,dfs_sum)
    return dfs_sum

n = input() #row
m = input() #column
matrix = [raw_input().split() for _ in range(n)] 
cc = -1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "1":
            cc = max(cc, dfs(matrix,(i,j)))

print cc