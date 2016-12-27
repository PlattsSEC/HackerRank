# Python 2.7
import sys
sys.setrecursionlimit(3000000)
n = input()
# Graph
g = {k:set() for k in xrange(1,2*n+1)}

# DFS stuff
visited = set()

def dfs(g,s,S=set(),dfs_sum=0):
    S.add(s)
    dfs_sum +=1
    for i in g[s]:
        if i in S: continue
        dfs_sum = dfs(g,i,S,dfs_sum) 
    return dfs_sum

# Building the graph
for i in xrange(n):
    a,b = map(int,raw_input().split())
    g[a].add(b)
    g[b].add(a)
    
# Getting the max and min lengths of the connected components
max_len, min_len = 0, sys.maxint
for i in xrange(1,n+1):
    if i not in visited:
        v = dfs(g,i,visited)
        if v > 1:
            max_len, min_len = max(max_len, v), min(min_len, v)
print(str(min_len)+" "+str(max_len))