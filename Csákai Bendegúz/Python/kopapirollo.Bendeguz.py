import random
lehetosegek = ('Kő', 'Papír', 'Olló')
sajat_pontok = 0
gep_pontok= 0
kor = int(input('Hány kört játszunk? '))
while kor != gep_pontok + sajat_pontok:
    sajat = input('Kő, papír, olló: ')
    if sajat in lehetosegek: 
        gep = random.choice(lehetosegek)
        print(f'A tiéd: {sajat}, az enyém: {gep}')
        if sajat == gep:
            sajat_pontok += 1
            gep_pontok += 1
            print(f'Hát, ez döntetlen, {sajat_pontok}-{gep_pontok} az állás!')
        elif (gep == 'Kő' and sajat == 'Olló') or (gep == 'Papír' and sajat == 'Kő') or (gep == 'Olló' and sajat == 'Papír'):
            gep_pontok += 1
            sajat_pontok = sajat_pontok
            print(f'Én nyertem most! Az állás {sajat_pontok}-{gep_pontok}.')
        else:
            gep_pontok =  gep_pontok
            sajat_pontok += 1
            print(f'Te nyertél most! Az állás {sajat_pontok}-{gep_pontok}.')
else:
    print('Vége a játéknak')
