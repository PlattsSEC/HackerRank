N,M = map(int,raw_input().split())

# Store edges for removal later
edges = []

# Function to remove edges
def remove_edge(g,edge):
    g[edge[0]].remove(edge[1])
    g[edge[1]].remove(edge[0])

# Function to add edges
def add_edge(g,edge):
    g[edge[0]].add(edge[1])
    g[edge[1]].add(edge[0])
    
# Function to check if all connected components have even number of nodes
def rem_okay(rem_edge):
    okay = True
    for i in rem_edge:
        if i%2!=0:
            okay = False
            break
    return okay

# DFS 
def dfs(g,s,S=set(),total=0):
    S.add(s)
    total +=1
    for i in g[s]:
        if i in S: continue
        total = dfs(g,i,S,total)
    return total
# Tree
t = {k:set() for k in range(1,N+1)}

# Build the tree
for i in range(M):
    a,b = map(int,raw_input().split())
    edges.append((a,b))
    t[a].add(b)
    t[b].add(a)

# edge count
rem_edge,rem = [],0
# Data structure to store nodes already in a component
visited = set()
# Start removing edges
for i in edges:
    remove_edge(t,i)
    for j in t:
        if j in visited: continue
        v = dfs(t,j,visited)
        rem_edge.append(v)
    if rem_okay(rem_edge):
        rem += 1
    else:
        add_edge(t,i)
    rem_edge,visited = [],set()

print rem
    