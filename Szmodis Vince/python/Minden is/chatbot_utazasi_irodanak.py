hely=input('Hova szeretnél utazni: ')
print(f'Természetesen van utunk {hely} felé')
penz=input('Mennyi pénzed van az útra: ')
print(f'Az utazás {penz/3*2} Ft-ba kerül')
print('Az idegenforgami illeték összege: 5000 Ft')
print(f'A teljes út költsége: {penz/3*2+5000}')
ajanlat=input('Efogadod az ajánlatot? (I/N):')
if ajanlat=='N':
    print('Nem rögzített foglalást, viszontlátásra!')
elif ajanlat=='I':
    letszam=0