import random
alap_szamok = []
for i in range(5):
   alap_szamok.append(random.randint(1,90))
print(alap_szamok)
talalatok = 0
for i in range(5):
    user_szamok = int(input(f'Add meg az {i+1}. számod: '))
    for i in range(5):
        if user_szamok == alap_szamok[i]:
            talalatok += 1
print(f'{talalatok} találatod volt.')