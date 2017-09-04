from heapq import heappush, heappop
inf = float('inf')
# Update W first, (lower weight)
# Then update D
def relax(W,u,v,D):
    temp_cost = W[u][v] - D.get(u,inf)
    if temp_cost > 0:
        W[u][v],W[v][u] = temp_cost,temp_cost
    else:
        W[u][v],W[v][u] = 0,0
        
    d = D.get(u,inf) + W[u][v]
    if d < D.get(v,inf):
        D[v] = d
        return True

def dijkstra2(g,s):
    D,Q,S = {s:0}, [(0,s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S: continue
        S.add(u)
        for i in g[u]:
            relax(g,u,i,D)
            heappush(Q,(D[i],i))
    return D

N,E = map(int,raw_input().split())
g = {k:{} for k in xrange(1,N+1)}
for i in xrange(E):
    a,b,cost = map(int,raw_input().split())
    g[a][b]=cost
    g[b][a]=cost
try:
    print dijkstra2(g,1)[N]    
except KeyError:
    print "NO PATH EXISTS"