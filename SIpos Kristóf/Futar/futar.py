forras=open('Sipos Kristóf\\Futar\\futar.txt',mode='r',encoding='utf-8')
forras.readline()

nap_sorszam=[]
fuvarszam=[]
tavolsag=[]

for sor in forras:
    adat=sor.strip().split(' ')
    nap_sorszam.append(int(adat[0]))
    fuvarszam.append(int(adat[1]))
    tavolsag.append(int(adat[2]))
forras.close

adatok_szama=len(tavolsag)

# Feladat 1
print('1.Feladat')
leghosszabb_fuvar_nap_sorszam=0
leghosszabb_fuvar_tavolsag=0
leghosszabb_fuvar_sorszam=0

for i in range(adatok_szama):
    if tavolsag[i]>leghosszabb_fuvar_tavolsag:
        leghosszabb_fuvar_tavolsag=tavolsag[i]
        leghosszabb_fuvar_sorszam=fuvarszam[i]
        leghosszabb_fuvar_nap_sorszam=nap_sorszam[i]
print(f'A leghosszabb útja a hét {leghosszabb_fuvar_nap_sorszam}. napján volt a {leghosszabb_fuvar_sorszam}. útja és {leghosszabb_fuvar_tavolsag}km volt.')
# Feladat 2
print('2.Feladat')
a_het_3as_napjan_megtett_utak=[]
for i in range(adatok_szama):
    if nap_sorszam[i]==3:
        a_het_3as_napjan_megtett_utak.append(tavolsag[i])
print(f'A harmadik napon összesen {sum(a_het_3as_napjan_megtett_utak)}km utat tett meg.')
# Feladat 3
print('3.Feladat')
a_het_4es_napjan_megtett_fuvarok=[]
for i in range(adatok_szama):
    if nap_sorszam[i]==4:
        a_het_4es_napjan_megtett_fuvarok.append(fuvarszam[i])
print(f'A 4.napon a futár {len(a_het_4es_napjan_megtett_fuvarok)} utat járt meg.')
# Feladat 4
print('4.Feladat')
for i in range(adatok_szama):
    if tavolsag[i]>20:
        print('Volt a futarnak 20km-nél hosszabb útja')
        break
    elif i==adatok_szama:
        print('A futárnak nem volt 20km-nél hosszabb útja.')
# Feladat 5
print('5.Feladat')

futar_kimenet=open('Sipos Kristóf\\Futar\\futar-kimenet',mode='w',encoding='utf-8')
for i in range(adatok_szama):
    if fuvarszam[i]==1:
        futar_kimenet.write(str(nap_sorszam[i]))
        futar_kimenet.write('.nap: ')
        futar_kimenet.write(str(tavolsag[i]))
        futar_kimenet.write('km')
        futar_kimenet.write('\n')


