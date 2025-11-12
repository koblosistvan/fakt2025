import random
dobas_szam=random.randint(100,200)
dobasok=[]
for i in range(dobas_szam):
    dobasok.append(random.randint(1,6))
print(dobasok)
print(f'A dobások száma: {dobas_szam}')
print(f'A dobott számok összege: {sum(dobasok)}')
print(f'A dobott számok átlaga: {sum(dobasok)/dobas_szam:.1f}')
for i in range(dobas_szam):
    if dobasok[i] == 6:
        print('A listában volt 6-os dobás.')
        break
else:
    print('A listában nem volt 6-os dobás.')
szam = int(input('Adj meg egy megnézendő számot a dobások közül: '))
szam_ind = 0
for i in range(dobas_szam):
    if dobasok[i] == szam:
        szam_ind = i+1
        print(f'A dobások között ez a szám: {szam} itt található: {szam_ind}.')
for i in range(dobas_szam):
    if dobasok[i] == szam:
        szam_ind = i+1
        break
print(f'A dobások között ez a szám: {szam} itt található először: {szam_ind}.')
db_szam = 0
for i in range(dobas_szam):
    if dobasok[i] == 5:
        db_szam += 1
print(f'Az 5-ös szám a dobások között {db_szam}x fordult elő.') 
print(f'5-ös számok százalékos aránya: {(db_szam/dobas_szam)*100:.0f}%.')
prim = 0
for i in range(dobas_szam):
    if dobasok[i] % 2 != 0 and dobasok[i] != 1:
        prim += 1
print(f'Az prímek száma a dobások között {prim}.') 
print(f'A prímszámok százalékos aránya: {(prim/dobas_szam)*100:.0f}%.')
print(f'A legkisebb dobott szám {min(dobasok)} volt.')
print(f'A legnagyobb dobott szám {max(dobasok)} volt.')