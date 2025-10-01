x = 0
gyökdb = 0

while gyökdb < 3:
    if x**3-78*x**2+1787*x-11070 == 0:
        gyökdb += 1
        print(x)
    x += 1