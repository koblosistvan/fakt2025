uvegek = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3 ]

#2.feladat
bekert = int(input("Mari néni lekvárja (dl):"))

#3.feladat

max_uveg = uvegek[0]
max_uveg_index = 0
for i in range(len(uvegek)):
    if uvegek[i] > max_uveg:
        max_uveg = uvegek[i]
        max_uveg_index +=1
print(f'A legnagyobb üveg {max_uveg} és a {max_uveg_index}. a sorban')

#4. feladat

ossz = sum(uvegek)

if bekert < ossz:
    print('Elegendo uveg volt')
if bekert > ossz:
    print('Maradt lekvar')




