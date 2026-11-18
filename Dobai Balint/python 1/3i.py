import random

gondoltam = random.randint(1, 100)
tipp = -1
tippszám = 5
while tipp != gondoltam:
    tipp= int(input('Mi a tipped ? '))
    if tipp == gondoltam:
        print('eltaláltad')
    else:
        print('nem jo, probald ujra')
    if tipp < gondoltam:
        print('a szám nagyobb mint a tipped')
        tippszám-=1
        print(f'{tippszám} életed maradt')
    elif tipp > gondoltam:
        print('a szam kisebb mint a tipped')
        tippszám-=1
        print(f'{tippszám} életed maradt')
    else:
        print('eltalaltad')
    
    
    
