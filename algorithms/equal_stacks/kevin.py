#!/usr/bin/env python3
# Kevin Boyette


# h1 = [3, 2, 1, 1, 1]
# h2 = [4, 3, 2]
# h3 = [1, 1, 4, 1]

n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = map(int, [n1, n2, n3])
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]


def first_is_biggest(x, y, z): return x > y or x > z


def all_equal(x, y, z): return x == y and y == z

h1_total = sum(h1)
h2_total = sum(h2)
h3_total = sum(h3)

equal_height = False

while not equal_height:
    if first_is_biggest(h1_total, h2_total, h3_total):
        h1_total -= h1.pop(0)
    if first_is_biggest(h2_total, h1_total, h3_total):
        h2_total -= h2.pop(0)
    if first_is_biggest(h3_total, h1_total, h2_total):
        h3_total -= h3.pop(0)
    if all_equal(h1_total, h2_total, h3_total):
        equal_height = True

print(h1_total)
