forras=open('Szmodis Vince\\python\\futar.txt', mode='r',encoding='utf-8')
adatok_szama=int(forras.readline())

nap_sorszam=[]
fuvar_szam=[]
tav=[]

for sor in forras:
    adat=sor.strip().split(' ')
    nap_sorszam.append(int(adat[0]))
    fuvar_szam.append(int(adat[1]))
    tav.append(int(adat[2]))

def f(n):
    print(f'\n{n}. feladat')

f(1)
max_ut=tav[0]
max_ut_index=0
for i in range(adatok_szama):
    if max_ut<tav[i]:
        max_ut=tav[i]
        max_ut_index=i
print(f'A leghosszabb út: {nap_sorszam[max_ut_index]} nap, {fuvar_szam[max_ut_index]} fuvar - {max_ut} km.')

f(2)

ossz_harmadik_nap=0
for i in range(adatok_szama):
    if nap_sorszam[i]==3:
        ossz_harmadik_nap+=tav[i]
print(f'A harmadik napon összesen {ossz_harmadik_nap} km-t tett meg.')

f(3)
fuvar_szam_negyedik_nap=0
for i in range(adatok_szama):
    if fuvar_szam[i]==4:
        fuvar_szam_negyedik_nap+=1
print(f'A negyedik napon 13 fuvart teljesített.')

f(4)
for i in range(adatok_szama):
    if tav[i]>20:
        print(f'A futárnak volt 20 km-nél hosszabb útja.')
        break
else:
    print('A futárnak nem volt 20 km-nél hosszabb útja.')

kimenet=open('Szmodis Vince\\python\\fuvar-kimenet.txt', mode='w', encoding='utf-8')



for i in range(adatok_szama):
    for j in range(7):
        if nap_sorszam[i]==j:
            break
        kimenet.write(f'{j}. nap:\t{tav[i]}km\n')
