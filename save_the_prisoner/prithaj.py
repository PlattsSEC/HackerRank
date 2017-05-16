from collections import deque
file = open('input011.txt','r')
T = int(file.readline())
for i in xrange(T):
    N,M,S = map(int,file.readline().split())
    q,count = deque([x%(N+1) for x in xrange(S,S+N+1) if x%(N+1)!=0]),1
    #print q
    while count < M:
        q.append(q.popleft())
        count += 1
    print q.popleft()