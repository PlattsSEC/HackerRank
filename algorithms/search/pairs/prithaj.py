#!/usr/bin/python

if __name__ == "__main__":
    N, K = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    arr_set = set(arr)
    print sum((1 for i in arr if i+K in arr_set))
