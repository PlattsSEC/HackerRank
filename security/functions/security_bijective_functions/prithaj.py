n = input()
Y = map(int, raw_input().split())

if len(Y) == n and len(set(Y)) == len(Y):
    print "YES"
else:
    print "NO"