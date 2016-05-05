orig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = int(input())
for i in range(num):
    alpha = list(orig)
    key = input()
    cipher = input()
    tl = list(key)
    letters = []
    newAlpha = []
    for l in tl:
        if l not in letters:
            letters.append(l)
            alpha.remove(l)
    length = len(letters)
    count = 0
    t = []
    for y in range(length):
        t.insert(y, "")
        t[y] += letters[y]
        count = y;
        while count < len(alpha):
            t[y] += alpha[count]
            count += length
    t.sort()
    for tt in t:
        for ttt in tt:
            newAlpha.append(ttt)
    count = 0
    for c in cipher:
        if(c != " "):
            print(orig[newAlpha.index(c)], end="")
            count += 1
            if(count == 5):
                count = 0
                print(" ", end="")
    print(" ")
