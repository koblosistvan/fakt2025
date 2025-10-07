kod = input('Add meg a kétszámjegyű kódot: ')
if int(kod[0]) % 2 == 0:
    if int(kod[1]) % 2 == 0:
        print('Belépés engedélyezve az 1-es szobába')
    else:
        print('Belépés engedélyezve az 2-es szobába')
else:
    if int(kod[1]) % 2 == 0:
        print('Belépés engedélyezve az 3-as szobába')
    else:
        print('Belépés engedélyezve az 4-es szobába')