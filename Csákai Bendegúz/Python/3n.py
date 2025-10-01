x = 0
megold = 0
while megold != 3:
    if x * -1 == abs(x):
        x += abs(x)+1
        a = int(x**3-78*(x**2)+1787*x-11070)
        if a == 0:
            megold += 1
            print(x)
    else:
        x *= -1
        a = int(x**3-78*(x**2)+1787*x-11070)
        if a == 0:
            megold += 1
            print(x)

