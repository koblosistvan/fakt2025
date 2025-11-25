forras=open('Sipos Kristóf\\python\\covid.txt', mode='r', encoding='utf-8')

fertozot=[]
halal=[]
idopont=[]
adatok=len(halal)

for sor in forras:
    adat=sor.strip().split(';')
    idopont.append(adat[0])
    fertozot.append(adat[1])
    halal.append(adat[2])
forras.close

#Feladat 1
print(f'1.Feladat\nAz állomány {adatok} nap adatait tartalmazza.')

#Feladat 2
fertozotak=0
halalok=0

for i in range(adatok):
    fertozotak+=fertozot[i]+fertozot[i-1]
    halalok+=halal[i]+halal[i-1]
print(f'\n2.Feladat\nA két év alatt az összes fertőzött száma {fertozotak} és az összes halott száma {halalok}.')

#Feladat 3
szaz_ezer_alatt=0
for i in range(adatok):
    if fertozot[i]< 100000:
        szaz_ezer_alatt+=1
print(f'\n3.Feladat \n A két évben {szaz_ezer_alatt} alkalommal volt a fertőzöttek száma 100,000 alatt')

for i in range(adatok-1):
    for j in range(adatok-1-i):
        if fertozot[j] < fertozot[j+1]:
            idopont[j], idopont[j+1] = idopont[j+1], idopont[j]
            fertozot[j], fertozot[j+1] = fertozot[j+1], fertozot[j]
            halal[j], halal[j+1] = halal[j+1], halal[j]

print(f'megbetegédi toplist:')
for i in range(5):
    print(f'{i+1}. {idopont[i]}: {fertozot[i]}')
