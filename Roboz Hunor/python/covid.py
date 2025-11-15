forras = open('fakt2025\\Roboz Hunor\\python\\covid.txt', mode='r', encoding='utf-8')
nap = []
regisztrált = []
halott = []
for sor in forras:
    adat = sor.strip().split(';')
    nap.append(adat[0])
    regisztrált.append(int(adat[1]))
    halott.append(int(adat[2]))
forras.close()
print('1. feladat')
print(f'Az állomány {len(nap)} nap adatait tartalmazza.')

össz_halal = 0
össz_regisztrált = 0
for i in range(len(nap)):
    össz_halal += halott[i]
    össz_regisztrált += regisztrált[i]
print('2. feladat')
print(f'A két év alatt összesen {össz_regisztrált:,} fertőzöttet és {össz_halal:,} halottat regisztráltak.')

e = 0
for i in range(len(nap)):
    if regisztrált[i] < 100000:
        e+=1
print('3. feladat')
print(f'A fertőzöttek száma {e} napon volt 100e fő alatt.')
legtöbb_halal = 0
fert = 0
c=0
for i in range(len(nap)):
    if halott[i] > legtöbb_halal:
        legtöbb_halal=halott[i]
        fert = regisztrált[i]
        c=nap[i]
print('4. feladat')
print(f'Legtöbben {c} napon haltak meg:\n\t{legtöbb_halal} fertőzött\n\t{fert} halott')
leg_arany = 0
b=0
for i in range(1,len(nap)):
    if regisztrált[i]/regisztrált[i-1]>b:
        leg_arany = i
        b = regisztrált[i]/regisztrált[i-1]
for i in range(len(nap)):   
    if i == leg_arany:
        leg_arany = nap[i]
print('5. feladat')
print(f'A legnagyobb arányú növekedés {leg_arany} napon volt, amikor az előző napi adat {b:.2f}-szorosa volt a fertőzöttek száma.')
  
nott = 0
csokkent=0
for i in range(len(nap)):
    if halott[i-1] < halott[i]:
        nott += 1
    elif halott[i-1] > halott[i]:  
        csokkent+=1
print('6. feladat')
print(f'A halálozások száma {csokkent} napon csökkent és {nott} napon nőtt az előző naphoz képest.')

print('7. feladat')
print(f'A napi halálozások átlagos száma {sum(halott)/len(halott):,.1f} volt.')



for i in range(len(nap)-1):
    for k in range(len(nap)-1-i):
        if regisztrált [k] < regisztrált[k+1]:
            regisztrált[k],regisztrált[k+1]=regisztrált[k+1],regisztrált[k]
            halott[k],halott[k+1]=halott[k+1],halott[k]
            nap[k],nap[k+1]=nap[k+1],nap[k]
print(f'Megbetegedési toplista:')
for i in range(5):
    print(f'\t{i+1}. {nap[i]} {regisztrált[i]}')