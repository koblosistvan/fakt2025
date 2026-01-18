forras = open('_Feladatok\\python\Fenyőfa\\fenyofa.txt',mode='r',encoding='utf-8')
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

a = 0

for sor in range(sorok):
    for betu in range(oszlopok):
        if karakterek[sor][betu] == 'b':
            a = sor
            break
    if karakterek[sor][betu] == 'b':
            break

b = 0

for sor in range(sorok):
    for betu in range(oszlopok):
        if karakterek[sor][betu] == 'b':
            b = sor

print(f'A fenyő teteje a {a+1}. sorban van, az alja a {b+1}.edik sorban')
print(f'A törzs {b-a+1} sor magas')

disz = 0

for sor in range(sorok):
    for betu in range(oszlopok-1):
        if karakterek[sor][betu] == 's' or karakterek[sor][betu] == 'p' or karakterek[sor][betu] == 'k':
                disz += 1

print(disz,'dísz van a fán')

alapszinek = 'hzbf'
szinek = {}


for sor in range(sorok):
     for betu in range(oszlopok):
          if karakterek[sor][betu] not in alapszinek:
               if karakterek[sor][betu] in szinek:
                    szinek[karakterek[sor][betu]] += 1
               else:
                    szinek[karakterek[sor][betu]] = 1

print(szinek)



# 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67