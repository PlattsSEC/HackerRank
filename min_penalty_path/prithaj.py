from heapq import heappush,heappop
inf = float('inf')

def relax(cost,u,v,D):
    d = D.get(u,inf) | cost
    if d < D.get(v,inf):
        D[v] = d
        return True
def dijkstra(g,s):
    D,q,S = {s:0},[(0,s)],set()
    while q:
        _,u = heappop(q)
        if u in S: continue
        S.add(u)
        for i in g[u]:
            if g[u][i]:
                for k in g[u][i]:
                    relax(k,u,i,D)
                    heappush(q,(D[i],i))
    return D

file = open('input13.txt','r')

N,M = map(int, file.readline().split()) 
g = {j:{k:[] for k in xrange(1,N+1)} for j in xrange(1,N+1)}
for i in xrange(M):
    a,b,cost = map(int,file.readline().split())
    g[a][b].append(cost)
    g[b][a].append(cost)
start,end = map(int,file.readline().split())
output = dijkstra(g,start)
try:
    print output[end]
except KeyError:
    print -1