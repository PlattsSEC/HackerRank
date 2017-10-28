#! /usr/bin/python3.5

n = eval(input())
def permutations(n):
    if n >= 1 and n <= 20:
        # n space-separated integers (2nd line of input; entered as strings), 
        # spaces removed and put into a list (split()), mapped as ints (map())
        # Put into new list because maps are not subscriptable
        y = list(map(int, input().split()))
        for i in range(n):
            # Subtract the number at index i of x by 1 to get the index where
            # its permutation is located
            print(y[(y[i]-1)])
    else:
        return 'Number must be between 1 and 20'
p = permutations(n)
p
