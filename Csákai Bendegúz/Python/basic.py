jegy = 1000
kor = int(input('Add meg a korodat: '))
hely = int(input('Helyi vagy? 1 = Igen, 2 = Nem: '))
nap = int(input('Nőnap van? 1 = Igen Bármi más = Nem: '))
if nap == 1:
    nem = int(input('Mi a nemed: 1 = Férfi 2 = Nő: '))     
    if nem == 1:    
        if hely == 1:
            jegy = jegy*0.8    
            if kor < 5:
                print('Ingyen bemehetsz kicsi')
            elif kor < 14 or kor > 65:
                print(f'Fizess {jegy*0.5:.0f} ft-ot ')
            elif kor > 14 or kor < 65:
                print(f'Fizess {jegy:.0f} ft-ot ')
        elif hely == 2:
            if kor < 14 or kor > 65:
                print(f'Fizess {jegy*0.5:.0f} ft-ot ')
            elif kor > 14 or kor < 65:
                print(f'Fizess {jegy:.0f} ft-ot ')
        else:
            print('Héló, ilyen szám nincs')
    else:
        print('Nőnap alkalmából te nőnek identifikált lény, ingyen bemehetsz')
else:
    if hely == 1:
        jegy = jegy*0.8    
        if kor < 5:
            print('Ingyen bemehetsz kicsi')
        elif kor < 14 or kor > 65:
            print(f'Fizess {jegy*0.5:.0f} ft-ot ')
        elif kor > 14 or kor < 65:
            print(f'Fizess {jegy:.0f} ft-ot ')
    elif hely == 2:
        if kor < 14 or kor > 65:
            print(f'Fizess {jegy*0.5:.0f} ft-ot ')
        elif kor > 14 or kor < 65:
            print(f'Fizess {jegy:.0f} ft-ot ')
    else:
        print('Héló, ilyen szám nincs')