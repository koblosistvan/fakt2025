import random

gondoltam= random.randint(1,100)

tipp = -1

while tipp != gondoltam:
    tipp=int(input('Mi a tipped? '))

    if tipp == gondoltam:
        print('Eltalátad')
    
    elif tipp < gondoltam:
        print('Enné nagyobb a gondot szám')

    elif tipp > gondoltam:
        print('Enné kisebb a gondot szám')    
    
    