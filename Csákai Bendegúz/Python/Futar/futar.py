forras = open('fakt2025\\Csákai Bendegúz\\Python\\Futar\\futar.txt', mode = 'r', encoding='utf-8')
adsz = forras.readline().strip()
nap = []
fuvar = []
km = []
for sor in forras:
    adat = sor.strip().split(' ')
    nap.append(int(adat[0]))
    fuvar.append(int(adat[1]))
    km.append(int(adat[2]))
forras.close()
print('\nAdatok beolvasása...')
print(f'A futar.txt fájlból beolvastam {adsz} sort.')

def f(n):
    print(f'\n{n}. feladat')

hossz = len(nap)
f(1)
index = 0
legh_ut = km[0]
for i in range(hossz):
    if km[i] > legh_ut:
        legh_ut = km[i]
        index = i
print(f'A leghosszabb út: {nap[index]}. nap, {fuvar[index]}. fuvar - {legh_ut} km.')
f(2)
harm_nap = []
for i in range(hossz):
    if nap[i] == 3:
        harm_nap.append(km[i])
print(f'A harmadik napon összesen {sum(harm_nap)}km-t tett meg.')
f(3)
negyed_fut = 0
for i in range(hossz):
    if nap[i] == 4:
        negyed_fut += 1
print(f'A negyedik napon {negyed_fut} fuvart teljesített.')
f(4)
for i in range(hossz):
    if km[i] > 20:
        print('A futárnak volt 20 km-nél hosszabb útja.')
        break
else:
    print('A futárnak nem volt 20 km-nél hosszabb útja.')
f(5)
for i in range(hossz):
    for j in range(hossz-i-1):
        if nap[i] < nap[i-1]:
            nap[i], nap[i-1] = nap[i-1], nap[i]
            km[i], km[i-1] = km[i-1], km[i]
            fuvar[i], fuvar[i-1] = fuvar[i-1], fuvar[i]

kimenet = forras = open('fakt2025\\Csákai Bendegúz\\Python\\Futar\\futar-kimenet.txt', mode = 'w', encoding='utf-8')
elso = 1
for i in range(hossz):
    if nap[i] == elso and fuvar[i] == 1:
        print(f'Napi első fuvarok:\n{elso}. nap: {km[i]} km', file=kimenet)
        elso += 1