import random

dobások=[]

for i in range(100):
    dobások.append(random.randint(1,6))

print (dobások)

hatosok_száma = 0

for i in range(100):
    if dobások[i] == 6:
        hatosok_száma+=1

print(f'A hatosok száma: {hatosok_száma}')