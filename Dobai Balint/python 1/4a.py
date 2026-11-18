import random

dobasok = []
for i in range(100):
    dobasok.append(random.randint(1,6))
print(dobasok)

hatosok_szama = 0
for i in range(len(dobasok)):
    if dobasok[i] == 6:
        hatosok_szama += 1

print(f'a dobasok között {hatosok_szama} hatos van')

for dobas in dobasok:
    if dobas == 6:
        hatosok_szama += 1

parosok_szama = 0
paratlanok_szama = 0 
for i in range(len(dobasok)):
    if dobasok[i] % 2 == 0:
        parosok_szama += 1
    else:
        paratlanok_szama += 1

print(f'{parosok_szama} paros van es {paratlanok_szama} paratlan van')

primek_szama = 0 
primszamok = [2,3,5]
for i in range(len(dobasok)):
    if dobasok[i] in primszamok:
        primek_szama += 1 

print(f'{primek_szama} primszam van')

egyketto_szama = 0 
for i in range (len(dobasok) -1 ):
    if dobasok[i] ==1 and dobasok [i+1] == 2:
        egyketto_szama += 1

print(f'{egyketto_szama} esetben fordul elo')

nagyobb_elozo = 0
for i in range(len(dobasok)-1):
    if dobasok[i] > dobasok[i+1]:
        nagyobb_elozo += 1

print(f'{nagyobb_elozo} esetben fordul elo')

szamlalok = [0,0,0,0,0,0]
for i in range(len(dobasok)):
    szamlalok[dobasok[i] -1] += 1 

print(szamlalok)


        
