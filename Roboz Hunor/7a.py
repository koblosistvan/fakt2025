forras = open('fakt2025\\_Feladatok\\python\\7a-lakas-arak.txt', mode='r', encoding='utf-8')

a = forras.readline()
ter = []
ar = []
for sor in forras:
    adat = sor.strip().split(' ')
    ter.append(int(adat[0]))
    ar.append(int(adat[1]))
forras.close()

legnagyobb_ar = ar[0]
legnagyobb_index = 0

for i in range(len(ar)):
    if ar[i] > legnagyobb_ar:
        legnagyobb_ar = ar[i]
        legnagyobb_index = i
print(f'A legdrágább lakás {legnagyobb_ar} millióba kerül és {legnagyobb_index}. a listában')

for i in range(len(ar)):
    if ar[i] >= 500:
        print('Van 500 milliónál többe kerülő lakás')
else: print('Nincs 500 milliónál többe kerülő lakás')


negyzetarany = 0
negyzetarany_index = 0

for i in range(len(ar)):
    b = ar[i] / ter[i]
    if b > negyzetarany:
        negyzetarany = b
        negyzetarany_index = i
print(f'{negyzetarany_index}. a listában')


huszalatt = 0
for i in range(len(ar)):
    if ar[i] < 20:
        huszalatt += 1
print(f'{huszalatt} db ház van ami 20 millió alatt van')



árak = open('fakt2025\Roboz Hunor\python\árak', mode='w', encoding='utf-8')
c = []
d = []

for i in range(len(ar)):
    if 50 < ar[i] < 60:
        c.append(ar[i])
        d.append(ter[i])
print(f'A lakások árai: {c} területei: {d} amik 50 és 60 millió között vannak',file=árak)



intervallum = int(input('Adj meg egy ártartományt amiben vásárolni szeretnél (pl.:50:60): ')).strip().split(':')

kezd = intervallum[0]
vég = intervallum[1]


for i in range(len(ar)):
    if kezd < ar[i] < vég:
        print(f'{ter[i]} {ar[i]} ')
