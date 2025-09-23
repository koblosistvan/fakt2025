import random

dobasok = []

for i in range(1, 101):
    dobasok.append(random.randint(1, 6))


hatosak = 0
for i in range(len(dobasok)):
    
    if dobasok[i] == 6:
        hatosak += 1
print(f"\n{hatosak} hatos dobás volt\n")