def ido(ora, perc, mp):
    return 3600 * ora + 60 * perc + mp

ora = int(input('Óra: '))
perc = int(input('perc: '))
mp = int(input('mp: '))

ido1 = ido(ora, perc, mp)

ora = int(input('Óra: '))
perc = int(input('perc: '))
mp = int(input('mp: '))

ido2= ido(ora, perc, mp)

if ido1 > ido2:
    print(f'Az első idő nagyobb {ido1-ido2} másodperccel')
elif ido1 == ido2:
    print('A két időpont egyenlő')
else:
    print(f'Az második idő nagyobb {ido2-ido1} másodperccel')





ido = input('Mennyi az idő? ').split()

print(ido)




