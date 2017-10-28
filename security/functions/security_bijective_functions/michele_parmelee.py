n = eval(input())
def checkBijective(n):
    if n >= 1 and n <= 20:
        vals = input()
        vals = vals.split()
        if len(vals) == n:
            seen = set()
            for v in vals:
                if v in seen:
                    return 'NO'
                seen.add(v)
            return 'YES'
        else:
            return('NO')
    else:
        print('Number must be between 1 and 20')
check = checkBijective(n)
print(check)
