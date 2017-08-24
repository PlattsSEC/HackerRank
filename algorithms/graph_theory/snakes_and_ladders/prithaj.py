T = input()
# BFS
def bfs(g,s):
    q,S = [], set()
    dist = {k:-1 for k in range(1,101)}
    dist[s] = 0
    S.add(s)
    q.append(s)
    while q:
        current_node = q.pop(0)
        for i in g[current_node]:
            if i in S: continue
            q.append(i)
            S.add(i)
            dist[i] = dist[current_node] + 1
    return dist

for i in range(T):
    # Board
    g = {k:set([j+k for j in range(1,7) if j+k<101]) for k in range(1,101)} 
    N = input()
    # Loop for ladders
    for j in range(N):
        a,b = map(int, raw_input().split())
        g[a] = set()
        x = a-6
        if x>0:
            for k in range(x,a):
                if a in g[k]:
                    g[k].remove(a)
                    g[k].add(b)
        else:
            for k in range(1,a):
                if a in g[k]:
                    g[k].remove(a)
                    g[k].add(b)
    
    M = input()
    # Loop for snakes
    for j in range(M):
        a,b = map(int, raw_input().split())
        g[a] = set()
        x = a-6
        if x>0:
            for k in range(x,a):
                if a in g[k]:
                    g[k].remove(a)
                    g[k].add(b)
        else:
            for k in range(1,a):
                if a in g[k]:
                    g[k].remove(a)
                    g[k].add(b)

    shortest_path = bfs(g,1)
    print shortest_path[100]