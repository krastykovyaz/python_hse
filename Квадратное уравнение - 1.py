from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('')
else:
    x1 = (- b + (sqrt(d))) / (2 * a)
    x2 = (- b - (sqrt(d))) / (2 * a)

    if x1 * 10 % 10 != 0:
        if x1 > x2:
            print(x2, x1)
        elif x1 == x2:
            print(x1)
        else:
            print(x1, x2)
    else:
        if x1 > x2:
            print(int(x2), int(x1))
        elif x1 == x2:
            print(int(x1))
        else:
            print(int(x1), int(x2))
