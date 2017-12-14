#!/bin/python
n, arr = input(), sorted(map(int, raw_input().split()))
print min((abs(x-y) for x,y in zip(arr,arr[1:])))