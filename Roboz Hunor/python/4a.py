import random
dobasok = []

for i in  range(100):
    dobasok.append(random.randint(1,6))

print(dobasok)

hatosok_szama= 0
for i in range (len(dobasok)):
    if dobasok[i] == 6:
        hatosok_szama+=1
print(f'A dobások között enyi hatos volt: {hatosok_szama}')