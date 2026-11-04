hova = input('Hova szeretnel menni?: ')
if hova == 'Miami':
    print('termeszesen van utunk oda')
else:
    print('nincs utunk oda')

penz = int(input('mennyi penzed van az utazasra?'))
penz2 = penz/3*2
print(f'az utazas ara {penz2}')
print('az idegenforgalmi ado 5000 Ft.')

teljes_penz = penz2 + 5000
print(f'az utazas vegosszege igy: {teljes_penz}')
dontes = input('elfogadod? (Igen/Nem) ? : ')
if dontes =='Nem':
    print('Rendben, nem foglalok utazast, viszlat')
if dontes == 'Igen':
    int(input('hany fo utazna?'))
        