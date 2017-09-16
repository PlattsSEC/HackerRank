#!/usr/bin/env python3
# Kevin Boyette

import sys


# h1 = [3, 2, 1, 1, 1]
# h2 = [4, 3, 2]
# h3 = [1, 1, 4, 1]

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = map(int, [n1,n2,n3])
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

equal_height = False
cylinder_totals = [sum(item) for item in [h1, h2, h3]]
while not equal_height:
    if cylinder_totals[0] > cylinder_totals[1] or cylinder_totals[0] > cylinder_totals[2]:
        cylinder_totals[0] -= h1.pop(0)
    if cylinder_totals[1] > cylinder_totals[0] or cylinder_totals[1] > cylinder_totals[2]:
        cylinder_totals[1] -= h2.pop(0)
    if cylinder_totals[2] > cylinder_totals[0] or cylinder_totals[2] > cylinder_totals[1]:
        cylinder_totals[2] -= h3.pop(0)
    if cylinder_totals[0] == cylinder_totals[1] and cylinder_totals[1] == cylinder_totals[2]:
        equal_height = True


print(cylinder_totals[0])
