szamla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]

von = 0
utal = 0
for  i in range(len(szamla)):
    if szamla[i] < 0:
        von += 1
    else:
        utal += 1
print("A számláról", von, "összeg lett levonva és", utal, "összeg lett jóváírva.")
levonas = 0
utalás = 0
for i in range(len(szamla)):
    if szamla[i] < 0:
        levonas += szamla[i]
    else:
        utalás = szamla[i]
print("A levonások összege:", levonas)
print("A jóváírások összege:", utalás)

apro = 0
összapro = 0
for i in range(len(szamla)):
    if szamla[i] % 1 !=0:
        apro+=1
        összapro += szamla[i]
print(f'Összesen {apro}x utaltak a szamlára apropénzes összeget')
print(f'A jóváírások aprópénzes összege: {összapro:2f}')

szaz = 0
for i in range(len(szamla)):
    if szamla[i] >= 100:
        szaz += 1
print(f'Összesen {szaz}x utaltak a számlára 100 egynél nagyobb összeget')
legnagyobb_jóváírás = max(szamla)
legnagyobb_levonás = min(szamla)
legkisebb_jóváírás = 0
for i in range(len(szamla)):
    if szamla[i] > 0 and (legkisebb_jóváírás == 0 or szamla[i] < legkisebb_jóváírás):
        legkisebb_jóváírás = szamla[i]
print(f'A legnagyobb jóváírás: {legnagyobb_jóváírás}')
print(f'A legnagyobb levonás: {legnagyobb_levonás}')
print(f'A legkisebb jóváírás: {legkisebb_jóváírás}')

hanyadik = 0
for i in range(len(szamla)):
    if szamla[i] == 50:
        hanyadik = i + 1 
        break
print(f'Az 50 eurós jóváírás a {hanyadik}. tranzakciónál történt.')

lev_nélkül_hanyadik = 0
for i in range(len(szamla)):
    if szamla[i] > 0:
        lev_nélkül_hanyadik += 1
    if szamla[i] == 50:
        break
print(f'Az 50 eurós jóváírás a {lev_nélkül_hanyadik}. tranzakció levonás nélkül.')

ki_lehet_venni = 'Nincs'
for i in range(len(szamla)):
    if szamla[i] %10 == 0:
        ki_lehet_venni = 'Van'
        break
print(f'{ki_lehet_venni} a számlán tízesével kivehető összeg.')


print(f'A számla egyenlege 0.75 eurós levonással: {sum(szamla)-0.75*len(szamla)} euró.')


hetvenöt_levon_utalasnal = sum(szamla)

for i in range(len(szamla)):
    if szamla[i] > 0:
        hetvenöt_levon_utalasnal -=0.75
print(f'A számla egyenlege 0.75 eurós levonással: {hetvenöt_levon_utalasnal} euró.')

