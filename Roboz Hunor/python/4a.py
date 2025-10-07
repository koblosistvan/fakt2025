import random
dobasok = []

for i in  range(100):
    dobasok.append(random.randint(1,6))

dobas = random.randint(1, 6)

print(dobasok)

hatosok_szama= 0
for i in range (len(dobasok)):
    if dobasok[i] == 6:
        hatosok_szama+=1
print(f'A dobások között enyi hatos volt: {hatosok_szama}')

parosok_szam = 0
for i in range(len(dobasok)):
    if dobasok[i] % 2 == 0:
        parosok_szam += 1
print(f'{parosok_szam} darab páros dobás volt')
print(f'{len(dobasok)-parosok_szam} darab páratlan dobás volt')



primszamok = [2,3,5]
prim_darab = 0
for i in range(len(dobasok)):
    if dobasok[i] in primszamok:
        prim_darab += 1
print(f'{parosok_szam} darab prím dobás volt')

egy_utan_ketto = 0
for i in range (len(dobasok)-1):
    if dobasok[i] == 1 and dobasok[i+1] == 1:
        egy_utan_ketto += 1
print(f'{egy_utan_ketto} x fordult elő hogy egy után kettő jött')



nagyobb_mint_az_elozo = 0


for i in range (len(dobasok)-1):
    if dobasok[i] < dobasok[i+1]:
        nagyobb_mint_az_elozo += 1
print(f'{nagyobb_mint_az_elozo} x fordult elő hogy a következő dobás nagyobb volt mint az előző')



szamlalok = [0,0,0,0,0,0]
for i in range(len(dobasok)):
    szamlalok[dobasok[i]-1] +=1
print(szamlalok)



print('Dobások: ')
for i in range(len(szamlalok)):
    print(f'\n\t{[i+1]}\t{szamlalok[i]}')