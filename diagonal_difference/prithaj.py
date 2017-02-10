n,s1,s2 = input(),0,0
for i in xrange(n):
    a = map(int,raw_input().split())
    s1,s2 = s1 + a[i],s2 + a[-(i+1)]
print abs(s1-s2)