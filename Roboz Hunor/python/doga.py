import random
szam = random.randint(100,120)
dobas = []
for i in range(szam):
    dobas.append(random.randint(1,6))
print(f'A szimuláció során {szam} dobás történt.')
ö = 0 
for  i in range(szam):
    ö+=dobas[i]
print(f'A dobott számok összege {ö}.')
print(f'A dobott számok átlaga {ö/szam:.1f}.')
for i in range(szam):
    if dobas[i] == 6:
        print('A listában volt hatos dobás.')
        break
else:
    print('A listában nem volt hatos dobás.')

#index = 0
#for i in range(szam):
#    if dobas[i] == 4:
#        index = i
#        break
#print(f'A dobások között a 4 első előfordulása: {index}.')

index = 0
a = int(input('Melyik szám első előfordulását keressem? '))
for i in range(szam):
    if dobas[i] == a:
        index = i
        break
print(f'A dobások között a {a} első előfordulása: {index}.')


b = []
for i in range(szam):
    if dobas[i] == a:
        b.append(i)
print(f'A dobások előfordulásai: {b}.')


c = 0
for i in range(szam):
    if dobas[i] == 3:
        c+=1
print(f'A dobások között {c} alkalommal fordult elő hogy a dobott szám 3 volt.')


d = 0
for i in range(szam):
    if dobas[i] == 2 or dobas[i] ==3 or dobas[i] == 5:
        d+=1
print(f'A dobások között {d} alkalommal fordult elő hogy a dobott szám prím volt, ez {d/szam*100:.0f}%-a a dobásoknak.')

legkisebb =6
legnagyobb = 1
for i in range(szam):
    if dobas[i] < legkisebb:
        legkisebb=dobas[i]
    elif dobas[i] > legnagyobb:
        legnagyobb=dobas[i]

print(f'A legkisebb dobott szám a {legkisebb}, a legnagyobb a {legnagyobb}.')

#print(f'A legkisebb dobott szám a {min(dobas)}, a legnagyobb a {max(dobas)}')

