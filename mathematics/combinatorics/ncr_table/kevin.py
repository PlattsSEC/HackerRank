#!/usr/bin/env python

# https://www.hackerrank.com/challenges/ncr-table


def get_number():
    return int(input().strip())


def nCr(row_number):
    rows = [[1], [1, 1], [1, 2, 1]]
    while row_number >= len(rows):
        # 1
        # 1 1
        # 1 2 1
        # 1 4 4 1
        # .......
        row = [(rows[-1][index] + rows[-1][index + 1])
               for index in range(len(rows) - 1)]
        rows.append([1] + row + [1])

    # Spew elements with * to show the proper output
    print(*rows[row_number])


# Generate this row from the nCr table
inputs = []
number_of_items = get_number()
for i in range(number_of_items):
    pascals_row = get_number()
    inputs.append(pascals_row)
print()
[nCr(item) for item in inputs]
