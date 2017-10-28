m = input()
c = ""
if len(m) >= 1 and len(m) <= 10:
    for i in range(len(m)):
        if m[i] == "9":
            c = c + "0"
        else:
            s = eval(m[i])
            c = c + str(s+1)
    print(c)
else:
    print('Number must be between 1 and 10')
