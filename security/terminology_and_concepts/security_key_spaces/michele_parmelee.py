#! /usr/bin/python3.5

m = input()
e = eval(input())
c = ""
if len(m) >= 1 and len(m) <= 10:
    if e >= 0 and e <= 9:
        for i in range(len(m)):
            # Turn each string into an actual number
            s = eval(m[i])
            # Add the value of e to shift 
            shift = s+e
            # But if the shift overflows past 10...
            if shift >= 10:
                # ...mod 10 takes the digit back to 0,
                # then counts up through 9 again
                shift = shift % 10
            c = c + str(shift)
                
        print(c)
    else:
        print('Number must be between 0 and 9')
else:
    print('String size must be between 1 and 10')
