# With a black box
from collections import deque as D
q = input()
queue = D()
for i in xrange(q):
    query = raw_input()
    if query[0] == '1':
        x = query.replace("1 ","")
        queue.append(x)
    elif query[0] == '2':
        queue.popleft()
    else:
        print queue[0]