import random

gondoltam = random.randint(1, 100)
tipp = -1           # olyan kezdőérték kell, ami biztosan nem a gondolt szám

while tipp != gondoltam:
    # megkérdezzük a tippet
    tipp = int(input('Mi a tipped: '))

    # ellenőrizzük, kiírunk egy választ
    if tipp > gondoltam:
        print('Sajnos nem jó, írj nagyobbat!')
    elif tipp < gondoltam:
        print('Sajnos nem jó, írj kisebbet!')
    elif tipp < 1 or tipp > 100:
        print('Na ne szórakozz!')
    else:
        print('Gratulálok, eltaláltad!!! ')
