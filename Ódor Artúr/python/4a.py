import random

dobasok = []

for i in range(1, 101):
    dobasok.append(random.randint(1, 6))


hatosak = 0
for i in range(len(dobasok)):
    
    if dobasok[i] == 6:
        hatosak += 1
print(f"\n{hatosak} hatos dobás volt\n")
egy_utan_ketto = 0
for i in range(1, len(dobasok) + 1):

print(f"{egy_utan_ketto} ször volt 1 után 2\n")