import random
b = []
szam = random.randint(1, 100)
ossz = 0
for i in range(1, szam):
    b.append(random.randint(1,10))
    if b[i] == 0:
        exit()
    else:
        if b[i] % 2 != 0:
            ossz += b[i]
            b[i] += 1
        else:
            b[i] += 1
print(ossz)

print(b)