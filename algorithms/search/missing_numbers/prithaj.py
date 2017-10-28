#!/bin/python
from collections import Counter


if __name__ == "__main__":
    n = input()
    A = Counter(raw_input().split())
    m = input()
    B = Counter(raw_input().split())

    result = []
    for i in B:
        try:
            if B[i] != A[i]:
                result.append(i)
        except:
            result.append(i)

    result.sort()       
    print " ".join(result)