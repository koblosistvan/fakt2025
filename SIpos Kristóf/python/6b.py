forras=open('Sipos Kristóf\\python\\6b-forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

hely=[]
ora=[]
perc=[]
ido=[]

for sor in forras:
    adat=sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close()

meresek_szama=len(hely)

legnagyobb= ido[1]-ido[0]
legnagyobb_index=0

for i in range(1,meresek_szama):
    if ido[i]-ido[i-1] > legnagyobb:
        legnagyobb = ido[i] - ido[i-1]
        legnagyobb_index = i
kezdete=f'{ora[legnagyobb_index-1]:0>2d}:{perc[legnagyobb_index-1]:0>2d}'
vege=f'{ora[legnagyobb_index]:0>2d}:{perc[legnagyobb_index]:0>2d}'

print(f'A legtöbb idő ami eltelt két áthaladás között az {kezdete} és {vege} között volt {legnagyobb} perc.')

hely_50=0
for i in range(1, meresek_szama):
    if 50==hely[i]:
        hely_50+=1
print(f'Az 50-es helyen {hely_50} szer mentek át.')

# adatbekérés
ora_input=int(input('Add meg melyik órába: '))
perc_input=int(input('Add meg melyik percben: '))
# validálás (jók-e a beírta adatok)
if ora_input > 24 or perc_input> 60:
    print('Ismered te az órát?')
# számolás
else:
    for i in range(1, meresek_szama):
        if ora_input == ora[i] and perc_input == perc[i]:
            print(f'Volt {ora_input}:{perc_input}-kor mérés.')
            break
    else:
        print(f'{ora_input}:{perc_input}-kor nem volt mérés.')

for i in range(1, meresek_szama):
    if ora[i-1] == ora[i] and perc[i-1] == perc[i]:
        print('Volt olyan mérés ami ugyan abba az időben volt.')
        break
else:
    print('Nem volt ilyen')

szamlalok=[0]*101
for i in range(1, meresek_szama):
    szamlalok[hely[i]] += 1
print(szamlalok)

legtobb= szamlalok[0]
legtobb_index=0

for i in range(len(szamlalok)):
    if szamlalok[i] > legtobb:
        legtobb = szamlalok[i]
        legtobb_index=i
print(f'A letöbbször a {legtobb_index+1}. helyen mentek át és {legtobb} szor.')