def idő(óra, perc, mp):
    return 3600*óra+60*perc+mp

print('Add meg az első időt:')

óra=int(input('Óra: '))
perc=int(input('Perc: '))
mp=int(input('Másodperc: '))

idő1 = idő(óra, perc, mp)

print('Add meg a második időt:')

óra=int(input('Óra: '))
perc=int(input('Perc: '))
mp=int(input('Másodperc: '))

idő2 = idő(óra, perc, mp)

if idő1>idő2:
    print(f'Az első idő nagyobb {idő1-idő2} másodpercel.')
elif idő1<idő2:
    print(f'A második idő nagyobb {idő2-idő1} másodpercel.')
else:
    print('A 2 idő megegyezik')