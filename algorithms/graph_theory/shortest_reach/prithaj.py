#Python 3.x
from collections import deque
EDGE_DISTANCE = 6
def bfs(g,s):
    S,q,dist = set(),deque(),{k:-1 for k in range(1,len(g)+1)}
    S.add(s)
    q.append(s)
    dist[s] = 0
    while q:
        current_node = q.popleft()
        for i in g[current_node]:
            if i in S: continue
            S.add(i)
            q.append(i)
            dist[i] = dist[current_node] + EDGE_DISTANCE
    return dist

queries = eval(input())
for i in range(queries):
    n,m = map(int,input().split())
    g = {k:set() for k in range(1,n+1)}
    for j in range(m):
        a,b = map(int,input().split())
        g[a].add(b)
        g[b].add(a)
    start = eval(input())
    val = bfs(g,start)
    output = ""
    for k in val:
        if k!= start:
            output = output + str(val[k])+ " "
    print(output)