forras = open('_Feladatok\\python\\Fenyőfa\\fenyofa.txt',mode='r',encoding='utf-8')
adat = forras.readline().strip().split()
oszlopok = int(adat[0])
sorok = int(adat[1])

karakterek = []

for i in range(sorok):
    adat = forras.readline().strip()
    karakterek.append(adat)
forras.close()

hópihe = 0

for sor in range(sorok):
    for betu in range(oszlopok):
        if karakterek[sor][betu] == 'f':
            hópihe += 1

print(hópihe,' darab hópihe van')
