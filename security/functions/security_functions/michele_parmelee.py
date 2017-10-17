#!/bin/python3

import sys

def calculate(x):
    # Complete this function
    try:
        if x >= 1 and x <= 1000:
            xr = x % 11
            return xr
        
    except ValueError:
        print("Input must be between 1 and 1000")

if __name__ == "__main__":
    x = int(input().strip())
    result = calculate(x)
    print(result)
