#!/usr/bin/env python


def get_matrix_row_from_input():
    return [int(index) for index in input().strip().split(' ')]


n = int(input().strip())
primary_diag_sum = 0
secondary_diag_sum = 0
for row_count in range(n):
    row = get_matrix_row_from_input()
    primary_diag_sum += row[row_count]
    secondary_diag_sum += row[-1 - row_count]

print(abs(primary_diag_sum - secondary_diag_sum))
