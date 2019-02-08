def betterBribes(q):
    num_bribes = 0

    for i, p in enumerate(q):
        #print(f'{i}, {p-1}')
        if (p-1) - i > 2:
            return 'Too chaotic'
        for j in range(max(p-2, 0), i):
            if q[j] > p-1:
                num_bribes += 1
    return num_bribes