n = int(input().strip())
value1 = 0
value2 = 0
for i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    value1 += a_t[i]
    value2 += a_t[-1-i]
print(abs(value2-value1))
