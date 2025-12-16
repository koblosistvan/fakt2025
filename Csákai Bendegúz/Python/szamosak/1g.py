#ido = input('Mennyi az idő: ').split()
#print(ido)

def ido(ora, perc, mp):
    return ora*3600+perc*60+mp
ora =  int(input('Ennyi óra van: '))
perc = int(input('Ennyi perc van: '))
mp = int(input('Ennyi másodperc van: '))

ido1 = ido(ora, perc, mp)

ora =  int(input('Ennyi óra van: '))
perc = int(input('Ennyi perc van: '))
mp = int(input('Ennyi másodperc van: '))

ido2 = ido(ora, perc, mp)

if ora < 24 and perc < 60 and mp < 60:
    if ido1 > ido2:
        print(f'Az 1. idő a nagyobb, {ido1-ido2} másodperccel')
    elif ido1 < ido2:
        print(f'Az 2. idő a nagyobb, {ido2-ido1} másodperccel')
    else:
        print('A 2 idő egyenlő')
else:
    print('Helyesen add meg az időt!')