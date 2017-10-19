n = eval(input())
def checkInverse(n):
    if n >= 1 and n <= 20:
        # The length, starting at 1, of n (1st line of input):
        y = list(range(1, n+1))
        # n space-separated integers (2nd line of input; entered as strings), 
        # spaces removed and put into a list (split()), mapped as ints and put into new list (map())
        # (no longer in order as typed because of map()):
        x = list(map(int, input().split()))
        # zip() creates tuples of x values aggregated to y values, saved as a new list:
        z = list(zip(x, y))
        # Sort numerically; i indicates the tuple, index 1 is the 2nd value of each tuple
        # where inverse is stored:
        for i in sorted(z):
            print(i[1])
    else:
        return 'Number must be between 1 and 20'
check = checkInverse(n)
check
