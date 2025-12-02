forras=open('Sipos Kristóf\\python\\imdb.txt', mode='r', encoding='utf-8')
forras.readline()
év=[]
időtartam=[]
értékelés=[]
rendező=[]
bevétel=[]
cím=[]
for sor in forras:
    adat=sor.split(' ')and sor.split('\t')

    év.append(int(adat[0]))
    időtartam.append(int(adat[1]))
    értékelés.append(float(adat[2]))
    rendező.append(adat[3])
    bevétel.append(int(adat[4]))
    cím.append(adat[5])
adatok_száma=(len(év))
#Feladat 1    
print(f'Ennyi adat van {adatok_száma}.' )
#Feladat 2
min_év=999999
első_film_neve=''
for i in range(adatok_száma):
    if min_év>év[i]:
        min_év=év[i]
        első_film_neve=cím[i]
print(f'Az első film {min_év} kor jelent meg és a neve: {első_film_neve} ')
#Feladat 3
Hosszabb_2_óránál=0
max_időtartam=0
for i in range(adatok_száma):
    if időtartam[i]>max_időtartam:
        max_időtartam=időtartam[i]
if max_időtartam-120>0:
    Van_2_óránál_hosszabb=True
elif max_időtartam-120<=0:
    Van_2_óránál_hosszabb=False
for i in range(adatok_száma):
    if Van_2_óránál_hosszabb==True:
        if időtartam[i]>120:
            Hosszabb_2_óránál+=1
    else:
        print('Nincs 2 óránál hosszabb film')
print(f'{Hosszabb_2_óránál} film van ami 2 óránál hosszabb')
#Feladat 4
for i in range(adatok_száma):
    if értékelés[i]>9.0:
        print('Van 9-nél nagyobb értékelés')
        break
    else:
        print('Nincsen 9-nél jobb értékelés.')
#Feladat 5
max_értékelés=0
for i in range(adatok_száma):
    if értékelés[i]>max_értékelés:
        max_értékelés=értékelés[i]
print(f'A legnagyobb értékelés a {max_értékelés} volt.')
#Feladat 6

#Feladat 7
legjobb_filmek=[]
legjobb_filmek_rendezőjei=[]
for i in range(adatok_száma):
    if max_értékelés==értékelés[i]:
        legjobb_filmek.append(cím[i])
        legjobb_filmek_rendezőjei.append(rendező[i])
print(f'A legjobb filmek {legjobb_filmek} voltak és a rendezőik {legjobb_filmek_rendezőjei} voltak.')
#Feladat 8
rendező=input('Adj meg egy rendezőt: ')
#Feladat 9
#Feladat 10
for i in range(adatok_száma):
    bevétel_átlag=sum(bevétel)//adatok_száma
print(f'Egy átlagos film bevétele {bevétel_átlag}.')
#Feladat 11
#Feladat 12