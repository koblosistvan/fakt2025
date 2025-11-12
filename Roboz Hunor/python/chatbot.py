a = input('hova szeretnél utazni')
print(f'Nyugodjon meg {a}-ra el tudjuk vinni')
b =int(input('mennyi pénzed van'))
print(f'Az utazás ára {b/3*2:.3f}, ezen felül 5000Ft forgalmi adót kell fizetnie')
c = input(f'Az utazás teljes ára: {b/3*2+5000:.3f}Ft. Elfogadja?')
if c == 'nem':
    print('Nem rögzítettem foglalást. Viszontlátásra')
elif c == 'igen':
    d = []
    e = int(input('Hány személy utazik'))
    f = input('Mik a az utasok nevei').strip().split(' ')
    for i in range(e):
        d.append(f[i])
    if 'Michael Jackson' in d:
        print('Michael Jackson ingyen utazik')
    elif 'Chuck Berry' in d:
        print('Chuck Berry ingyen utazik')
    print('rögzítettem foglalást. Viszontlátásra')