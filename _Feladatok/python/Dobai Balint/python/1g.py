def ido(ora, perc, mp):
    return 3600*ora+50*perc+mp
ora = int(input('ora'))
perc =int(input('perc'))
mp =int(input("masodperc"))


ora =int(input("ora"))
perc =int(input('perc'))
masodperc =int(input("mp"))

ido1 = ido(ora, perc, mp)

print(ido1)

ora = int(input('ora'))
perc =int(input('perc'))
mp =int(input("masodperc"))

ido2 =ido(ora, perc, mp)

if ido1 > ido2:
    print(f'az elso nagyobb {ido1-ido2} masodperccel')
elif ido1 < ido2:
   
    print(f'a masodik nagyobb{ido2-ido1} masodperccel')
else:
    print('a 2 idopont egyenlo')