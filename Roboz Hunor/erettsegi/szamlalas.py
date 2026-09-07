

def f(a):
    print(f'{a}. feladat')
    
    
forras = open('Roboz Hunor\\erettsegi\\meres.txt',mode='r',encoding='utf-8')
meresek = []
for sor in forras:
    adat = sor.split(', ')

for i in range(len(adat)):
    meresek.append(int(adat[i]))

ossz = len(meresek)

f(2)

szaml = 0

for i in range(ossz):
    if meresek[i] != -1:
        szaml += meresek[i]

print(f'Osszesen {szaml} kerekparost szamoltak.')


f(3)

hat,het,nyolc,kilenc = 0, 0, 0, 0

for i in range(ossz):
    if meresek[i] != -1:
        if 3 >= i:
            hat += meresek[i]
        if 7 >= i and i > 3:
            het += meresek[i]
        if 11 >= i and i > 7:
            nyolc += meresek[i]
        if i > 11:
            kilenc += meresek[i]
print(f'6 órától {hat} kerékpáros')
print(f'7 órától {het} kerékpáros')
print(f'8 órától {nyolc} kerékpáros')
print(f'9 órától {kilenc} kerékpáros')


f(4)

max_ertek = meresek[0]
max_hely = 0


for i in range(ossz):
    if meresek[i] > max_ertek:
        max_ertek = meresek[i]
        max_hely = i


ora = 6
perc = 0

for i in range(max_hely+1):
    print(ora,perc)
    if i % 4 == 3:
        ora += 1
        perc = 0
    else:perc += 15
    


print(f'Az áthaladók maximális száma: {max_ertek}; a rögzítés időpontja: {ora}:{perc}.')