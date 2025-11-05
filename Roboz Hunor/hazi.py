import random
létszám = random.randint(15,20)
osztályzat = []
db = 0
for i in range(létszám):
    osztályzat.append(random.randint(1,5))
    db+=1
atlag = sum(osztályzat)/db
print(f'A lista {db} elemet tartalmaz.')
print(f'Az osztályzatok összege {sum(osztályzat)}.')
print(f'Az osztályzatok átlaga {atlag:.1f}.')
for i in range(létszám):
    if osztályzat[i] == 1:
        print(f'A listában volt elégtelen osztályzat')
        break
else:
    print(f'A listában nem volt elégtelen osztályzat')
szam = int(input('Melyik osztalyzatra vagy kíváncsi'))
mennyi = 0
ossz = ''
for i in range(létszám):
    if osztályzat[i] == szam:
        mennyi = i
        ossz += f'{str(i)}, '
        if mennyi == 0:
            nincs = True
        else: nincs =False
else:
      print('Nincs ilyen szám')
for i in range(létszám):
    if osztályzat[i] == szam:
        m = i
a = []
for i in range(len(ossz)):
    a.append(ossz[i])
a[-2],a[-1] = '',''
ossz =''
for i in range(len(a)):
    ossz += a[i]
if nincs == True:
          print('Nincs ilyen osztályzat')
else:
     print(f'Az osztályzatok között a {szam} első előfordulása: {m}.')
     print(f'Az osztályzatok között a {szam} előfordulásai: {ossz}.')
valassz = int(input('valassz egy számot'))
előfordul= 0
for i in range(létszám):
    if osztályzat[i] == valassz:
        előfordul+=1
print(f'A {valassz} osztályzat {előfordul} alkalommal fordul elő.')
kozepesnel = 0
for i in range(létszám):
    if osztályzat[i] > 3:
        kozepesnel+=1
print(f'Az osztályzatok között a közepesnél {kozepesnel} darab osztályzat lett jobb')
print(f'A kozepesnel az osztályzatok {(kozepesnel/létszám*100):.2f}%-a lett jobb')
kicsi = 5
nagy = 1
for i in range(létszám):
    if osztályzat[i] > nagy:
        nagy = osztályzat[i]
    if osztályzat[i] < kicsi:
        kicsi = osztályzat[i]
print(f'A legkisebb osztályzat a {kicsi}, az legnagyobb az {nagy}')
#print(f'A legkisebb osztályzat a {min(osztályzat)}, az legnagyobb az {max(osztályzat)}')
