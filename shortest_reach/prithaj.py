queries = input()
EDGE_DISTANCE = 6

# BFS stuff
def bfs(g,s,S=set(),dist={}):
    q = []
    S.add(s)
    q.append(s)
    dist[s] = 0
    while q:
        current_node = q.pop(0)
        for i in g[current_node]:
            if i in S: continue
            S.add(i)
            q.append(i)
            if dist[i] == -1:
                dist[i] = dist[current_node] + EDGE_DISTANCE
    

for i in range(queries):
    n,m = map(int, raw_input().split())
    g = {k:set() for k in range(1,n+1)}
    for i in range(m):
        a,b = map(int,raw_input().split())
        g[a].add(b)
        g[b].add(a)
    s = input()
    
    # Keep track of visited nodes
    visited = set()
    # Initialize the distance data structure
    dist = {k:-1 for k in range(1,n+1)}
    
    # Find all connected components
    for i in xrange(1,n+1):
        if i in visited: continue
        bfs(g,s,visited,dist)
        
    # Print the distances
    result = ""
    for j in xrange(1,n+1):
        if j != s:
            result = result + str(dist[j]) + " "
    result = result.rstrip(" ")
    print result