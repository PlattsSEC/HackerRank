import sys
sys.setrecursionlimit(3000000)

N,l = map(int,raw_input().split())

#Graph
g = {k:set() for k in xrange(N)}

#DFS
def dfs(g,s,S=set(),tree_len=0):
    tree_len += 1
    S.add(s)
    for i in g[s]:
        if i in S: continue
        tree_len = dfs(g,i,S,tree_len)
    return tree_len

# Build the graph            
for i in xrange(l):
    a,b = map(int,raw_input().split())
    g[a].add(b)
    g[b].add(a)
    
# Store all visited nodes
visited = set()
# Store the lengths of the connected components
cc = []
# Get all the connected components
for i in g:
    if i not in visited:
        v = dfs(g,i,visited)
        cc.append(v)
    else:
        continue
        
# Calculate number of pairs
result, old_sum = 0, 0
for i in cc:
    result = result + old_sum * i
    old_sum = old_sum + i
print result