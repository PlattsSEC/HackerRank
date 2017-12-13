#!/bin/python

n, m = map(int, raw_input().split())
coins = map(int, raw_input().split())
cache = {}
def make_change(coins,n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m<=0 and n>=1:
        return 0
    if (n,m) in cache:
        return cache[(n,m)]    
    cache[(n,m)] = make_change(coins,n-coins[m-1],m)+make_change(coins,n,m-1)
    return cache[(n, m)]

print make_change(coins, n, m)