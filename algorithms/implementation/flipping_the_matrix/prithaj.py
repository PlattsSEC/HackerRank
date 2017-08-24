# Enter your code here. Read input from STDIN. Print output to STDOUT
q = input()   
for i in range(q):
    n = input()
    m = []
    for j in range(2*n):
        m.append(map(int,raw_input().split()))
    print sum([max(m[x][y],m[x][2*n-1-y],m[2*n-1-x][y],m[2*n-1-x][2*n-1-y]) for x in range(n) for y in range(n)])