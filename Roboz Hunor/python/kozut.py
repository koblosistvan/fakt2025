forras = open('_Feladatok\\python\\Közúti ellenőrzés\\kozut.txt',mode = 'r', encoding='utf-8')
sorok_szama = int(forras.readline())

ora,perc,mp,seb,rendsz = [],[],[],[],[]

for sor in forras:
    adat = sor.strip().split()
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    mp.append(int(adat[2]))
    seb.append(int(adat[3]))
    rendsz.append(adat[4]) 
forras.close()


def f(n):
    print(f'\n{n}. feladat')


f(1)


szaml = 0

for i in range(sorok_szama):
    if seb[i] > 50:
        szaml += 1

print(szaml,' autó volt gyorsabb a megengedett 50 km/h-nál.')


f(2)


for i in range(sorok_szama):
    if seb[i] > 55:
        print('Volt 55 km/h-nál gyorsabb autó.')
        break
    else: print('Nem volt 55 km/h-nál gyorsabb autó.')


f(3)


leg_gyors,leg_gyors_rendsz = 0, rendsz[0]

for i in range(sorok_szama):
    if seb[i] > leg_gyors:
        leg_gyors,leg_gyors_rendsz = seb[i], rendsz[i]
        
print(f'A leggyorsabb autó rendszáma: {leg_gyors_rendsz}, {leg_gyors} km/h sebességgel ment.')


f(4)


print(f'Az áthaladó autók átlagsebessége {sum(seb)/len(seb):.2f} km/h volt.')


f(5)


kimenet = open('Roboz Hunor\\python\\kozut-kimenet.tx', mode='w',encoding='utf-8')
print('30 km/h-nál lassabb járművekadatai',file=kimenet)

for i in range(sorok_szama):
    if seb[i] < 30:
        print(f'{ora[i]}:{perc[i]}:{mp[i]} - {rendsz[i]} - {seb[i]} km/h',file=kimenet)


f(7)


for i in range(sorok_szama-1):
    if seb[i] > 90 and seb[i+1] > 90:
        print('Volt "utcai verseny"')
        break
else:print('Nem volt "utcai verseny"')


f(8)        

a = {}

for i in range(sorok_szama):
    ido = f'{ora[i]}:{perc[i]}:{mp[i]}'
    if rendsz[i] not in a:
        a[rendsz[i]] = []
    a[rendsz[i]].append(ido)


'''for i in range(len(a)):
    rendszam = a[i]
    if len(a[rendszam]) > 1:
        print(rendszam, a[rendszam])
    
    '''
f(9)    


min_ido = 100000

for i in range(sorok_szama-1):
    t_ido = (ora[i+1]*3600 + perc[i+1]*60 + mp[i+1]) - (ora[i]*3600 + perc[i]*60 + mp[i]) 
    if t_ido < min_ido:
        min_ido = t_ido
print(f'A legrövidebb áthaladás {min_ido} másodperc alatt történt')



for i in range(sorok_szama):
    b = str(rendsz[i])
    db_kotojel = 0
    for k in range(len(b)):
        if b[k] == '-':
            db_kotojel += 1
    if db_kotojel == 3:
        print('Van új rendszám a listában')
        break
else:print('Nincs új rendszám a listában')


