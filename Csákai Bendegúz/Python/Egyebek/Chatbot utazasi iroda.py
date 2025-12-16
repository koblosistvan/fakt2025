hova = input('Adja meg hova szeretne utazni: ')
print(f'Nagyszerű választás! Ide ({hova}) el tudjuk vinni.')
money = int(input('Mennyit tud az útra szánni?: '))
uti = money/3*2
print(f'Szuper! Az utazás ára: {uti:.0f}Ft, valamint kell fizetnie még 5000Ft-ot forgalmi adó aránt.')
dontes = input(f'Az út teljes költsége: {uti+5000:.0f}Ft. Elfogadja? (igen/nem): ')
if dontes == 'nem':
    print('Ön nem rögzített foglalást. Viszlát!')
elif dontes == 'igen':
    szem_szam = int(input('Adja meg hány személy utazna: '))
    nevek_meg = input('Adja meg kik utaznak (,-vel és szóközzel elválasztva): ')
    nevek_list = []
    for i in range(len(nevek_meg)):
        nevek_list.append(nevek_meg.split(', '))
print(nevek_list)
#else:
#    print('Igennel vagy nemmel válaszoljon!')