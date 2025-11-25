
forras=open('Sipos Kristóf\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev=[]
szul_ho=[]
szul_nap=[]
kezdes_eve=[]
vegzes_eve=[]




adatok_szama=int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

életkor=int(input('Add meg az életkorod: '))
honap=int(input('Add meg melyik hónapban születtél:'))
nap=int(input('Add meg melyik napon születtél: '))

for i in range(adatok_szama):
    kor=vegzes_eve[i] - szul_ev[i]
    if kor < életkor:
        print(f'Van {életkor} évnél fiatalabb végzett.')
        break
else:
    print(f'Nincs {életkor} évnél fiatalabb végzet.')

#i=0
#while i< adatok_szama and vegzes_eve[i]-szul_ev[i] >= eletkor:
#    i+=1
#if i < adatok_szama:
#    print(f'Van {eletkor} évnél fiatalabb végzet.')
#else:
#    print(f'nincs {eletkor} évnél fiatalabb végzet.')

for i in range(adatok_szama):
    if honap == szul_ho[i] and szul_nap[i] == nap:
        print('Van olyan halgató akinek akkor van a születés napja mint neked.')
        break
else:
    print('Nincs olyan halgató akinek a születés napja az mint a tied.')

legfiatalabb_hallgato=vegzes_eve[i]-kezdes_eve[i]
legfiatalabb_hallgato_vegzes_ev=0

for i in range(1, adatok_szama):
    if legfiatalabb_hallgato:
        legfiatalabb_hallgato = szul_ev[i]
        legfiatalabb_hallgato_vegzes_ev = vegzes_eve[i]
print(f'A legfatalabb halgató {legfiatalabb_hallgato} -ban született és {legfiatalabb_hallgato_vegzes_ev}-ben végzet.')


vegeztek_2016=0

for i in range(1, adatok_szama):
    if vegzes_eve[i] == 2016:
        vegeztek_2016 += 1
print(f'2016-ban {vegeztek_2016} ember végzet.')
        