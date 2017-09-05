#!/bin/python

s, _, _ = map(int, raw_input().split())
N = map(int, raw_input().split())
M = map(int, raw_input().split())

try:
    print max([i+j for i in N for j in M if i+j<=s])
except ValueError:
    print -1