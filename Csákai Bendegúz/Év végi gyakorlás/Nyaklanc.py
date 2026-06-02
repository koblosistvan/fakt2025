#1
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-1.txt', mode = 'r', encoding= 'utf-8')
adat = forras.readline().strip()
adat = list(adat)
forras.close()
print(adat)
#2
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-2.txt', mode = 'r', encoding= 'utf-8')
adat = forras.readline().strip()
adat = adat.split()
forras.close()
print(adat)
#3
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-3.txt', mode = 'r', encoding= 'utf-8')
adat = []
for sor in forras:
    adat.append(sor.strip())
forras.close()
print(adat)
#4
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\1-gyongy-4.txt', mode = 'r', encoding= 'utf-8')
adat = []
int(forras.readline())
for sor in forras:
    adat.append(sor.strip())
forras.close()
print(adat)
'''# utolso par
forras = open('fakt2025\\_Megoldások\\python\\11 év végi gyakorlás\\1-gyongy-1-utolsó pár.txt', mode = 'r', encoding= 'utf-8')
adat = forras.readline().strip()
adat = list(adat)
forras.close()
print(adat)
'''
# hány féle van?
'''adat = ['S', 'P', 'L', 'S']'''
szinek = []
for i in adat:
    if i not in szinek:
        szinek.append(i)
print(f'{len(szinek)} db különböző színű gyöngy van rajta.')

#2
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        print('Előfordul')
        break
else:
    print('Nem fordul elő')

#3
print(adat)
m = int(input('Mennyire vagy kíváncsi?: '))
n = 0
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        n +=1
    else:
        n = 0
        i+=1
if n >= m:
    print(f'{m} előfordul egymás után')
else:
    print(f'{m} nem fordul elő egymás után')

