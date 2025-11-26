számla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
von = 0
u = 0
for  i in range(len(számla)):
    if számla[i] > 0:
        u +=1 
    elif számla[i] < 0:
        von += 1
print(f'{u} alkalommal utaltak és {von} alkalommal vontak le pénzt a számláról')


ö = 0
for  i in range(len(számla)):
    ö+=számla[i]
print(f'{ö} euro van a számlán')

a = 0

for  i in range(len(számla)):
    if számla[i] > 100:
        a += számla[i]

print(f'{a} esetben utaltak legalább száz eurót a számlára')

v = []
k = []

for  i in range(len(számla)):
    if számla[i] > 0:
        k.append(számla[i])
    elif számla[i] < 0:
        v.append(számla[i])
print(f'{max(v)} a legnagyobb levonás, {max(k)} a legnagyobb utalás {min(számla)} a legkisebb utalás')

ind = 0

for  i in range(len(számla)):
    if számla[i] == 225:
        ind=i
print(f'A {ind}. sorszámú utalás volt 225 euro')

for i in range(len(k)):
    if számla[i] == 225:
        ind=i
print(f'A {ind}. sorszámú utalás volt 225 euro ha nem számítjuk a levonásokat')


for i in range(len(k)):
    if számla[i] > 1000:
        print(f'Az 1000-nél nagyobb utalás az {i}. volt a listában')
else: print(f'Az 1000-nél nagyobb utalás nem volt a listában')


for  i in range(len(számla)):
    if számla[i] %10 ==0 :
        print('Van olyan összeg amit ki lehet venni bankautomatából')
else: print('Nincs olyan összeg amit ki lehet venni bankautomatából')


