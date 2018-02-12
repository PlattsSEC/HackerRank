n, d = map(int, raw_input().split())
arr = map(int, raw_input().split())
seq_set = set(arr)
print sum((1 for i in arr if d+i in seq_set and 2*d+i in seq_set))