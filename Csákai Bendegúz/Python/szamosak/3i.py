import random
megold = random.randint(1,100)
szam = -1
elet = 10
while (szam != megold) and (elet > 0):
    szam = int(input('Mondj egy számot 1-100-ig: '))
    if szam == megold:
        print('Szép')
        print(f'Ennyi próbálkozásod maradt: {elet-1}')
    elif szam < megold:
        print('Nagyobb')
        elet -= 1
        if elet == 5:
            print('Már csak 5 próbálkozásod maradt')
    else:
        print('Kisebb')
        elet -= 1
        if elet == 5:
            print('Már csak 5 próbálkozásod maradt')
    