def ido(ora,perc,mp):
    return 3600* ora + 60 * perc + mp


ora =int(input('óra: '))
perc =int(input('perc: '))
mp = int(input('másodperc: '))

ido1 = (ora,perc,mp)

ora =int(input('óra: '))
perc =int(input('perc: '))
mp = int(input('másodperc: '))

ido2= (ora,perc,mp)

if ido1 > ido2:
    print(f'Az első idő nagyobb {ido1-ido2} ennyivel')
elif ido1 == ido2:
    print('egyenlőek')
else:
    print(f'A második idó nagyobb {ido2-ido1} ennyivel')