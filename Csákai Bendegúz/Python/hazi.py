import random
letszam = random.randint(15,20)
osztalyzatok = []
for i in range(letszam):
    osztalyzatok.append(random.randint(1,5))
osszeg = sum(osztalyzatok)
print(osztalyzatok)
print(f'A lista {letszam} elemet tartalmaz')
print(f'Az osztályzatok összege: {osszeg}')
print(f'Az osztályzatok átlaga: {osszeg/letszam:.2f}')
egyes = 0
for i in range(letszam):
    if osztalyzatok[i] == 1:
        egyes += 1
print(f'Az 1-esek száma: {egyes}')
bekert_osztalyzat=int(input('Add meg hogy melyik osztályzatot szeretnéd megkeresni: '))
bekert_oszt_ind = 0
db_szam = 0
for i in range(letszam):
    if osztalyzatok[i] == bekert_osztalyzat:
        bekert_oszt_ind = i
        print(f'{bekert_oszt_ind+1}. jegy volt {bekert_osztalyzat}')
for i in range(letszam):
    if osztalyzatok[i] == 2:
        db_szam +=1
print(f'{db_szam} db 2-es jegy volt')
jobb_kozepesnel = 0
for i in range(letszam):
    if osztalyzatok[i] > 3:
        jobb_kozepesnel +=1
print(f'{jobb_kozepesnel} db jegy volt jobb 3-asnál, azaz a jegyek {jobb_kozepesnel/letszam*100:.0f}%-a (kerekítve) volt jobb')
print(f'{min(osztalyzatok)} volt a leggyengébb jegy, és {max(osztalyzatok)} volt a legjobb jegy (min/max-os)')
leggyengebb = osztalyzatok[0]
legerosebb = osztalyzatok[0]
for i in range(letszam):
    if osztalyzatok[i] < leggyengebb:
        leggyengebb = osztalyzatok[i]
    if osztalyzatok[i] > legerosebb:
        legerosebb = osztalyzatok[i]
print(f'{leggyengebb} volt a leggyengébb jegy, és {legerosebb} volt a legjobb jegy (ciklusos)') 