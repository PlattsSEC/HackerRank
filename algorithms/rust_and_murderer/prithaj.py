# Passes only 4/7 test cases.
# Needs more optimization

from collections import deque
T = input()

def add_edge(a,b,my_dict):
    if a in my_dict:
        my_dict[a].add(b)
    else:
        my_dict[a] = set()
        my_dict[a].add(b)
    if b in my_dict:
        my_dict[b].add(a)
    else:
        my_dict[b] = set()
        my_dict[b].add(a)

# BFS
def return_nodes(N,a,edges):
    for i in xrange(1,N+1):
        try:
            if i!=a and i not in edges[a]:
                yield i
        except KeyError:
            yield i

def bfs(start,N,edges):
    S,q,dist = set(),deque(),{}
    S.add(start)
    q.append(start)
    dist[start] = 0
    while q:
        current_node = q.popleft()
        for i in return_nodes(N,current_node,edges):
            if i in S: continue
            S.add(i)
            q.append(i)
            dist[i] = dist[current_node] + 1
    return dist
        
for i in xrange(T):
    N,M = map(int,raw_input().split())
    # Main roads/edges
    main_edges = {}
    for j in xrange(M):
        a,b = map(int,raw_input().split())
        add_edge(a,b,main_edges)       
    start = input()
    dist = bfs(start,N,main_edges)
    for k in dist:
        if k != start:
            print dist[k],
    print " "