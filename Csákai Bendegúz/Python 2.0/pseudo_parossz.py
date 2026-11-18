def parososszeg(c):
    ossz = 0
    for i in range(len(c)):
        if c[i] % 2 == 0:
            ossz += c[i]
    return ossz

print(parososszeg([5, 2, 6, 8, 3, 6]))