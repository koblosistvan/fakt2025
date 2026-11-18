import random

osztalyzatok = []
for i in range(16):
    osztalyzatok.append(random.randint(1,5))
print(osztalyzatok)
print('az osztalyzatok szama: ', len(osztalyzatok))

osszeg = 0


for i in range(len(osztalyzatok)):
    osszeg = sum(osztalyzatok)
print(osszeg)


atlag = osszeg / len(osztalyzatok)
print(f'az osztalyzatok atlaga: {atlag:.2f}')

elegtelen = osztalyzatok[0]


for i in range(len(osztalyzatok)):
    if osztalyzatok[i] ==1:
        print('van elegtelen osztalyzat az eredemenyek kozott')
        break
else:
    print('nincs elegtelen osztalyzat az eredmenyek kozott')



keresett = int(input('melyik osztalyzatot keressem(3,4,5)'))

darab = osztalyzatok.count(keresett)

print(f'a {keresett} osztalyzat {darab} alkalommal fordult elo')

harmas = osztalyzatok[0]
harmas_index = 0

for i in range(len(osztalyzatok)):
    if osztalyzatok[i] == 3:
        harmas_index += 1

print(f'harmas osztalyzat {harmas_index} alkalommal fordult elo')

harmasnal_jobb = osztalyzatok[0]
harmasnal_jobb_index = 0

for i in range (len(osztalyzatok)):
    if osztalyzatok[i] > 3:
        harmasnal_jobb_index +=1 

print(f'harmasnal jobb osztalyzat {harmasnal_jobb_index} alkalommal volt')

szazalek_atlag = harmasnal_jobb_index / len(osztalyzatok)


print(f'harmasnal jobb osztalyzatok szazalekos atlaga : {szazalek_atlag*100:.0f} %')
print(f'a legrosszabb osztalyzat {min(osztalyzatok)}, a legjobb pedig {max(osztalyzatok)}')

