import random
a = random.randint(1,100)
élet= 8
tipp = -1
while a != tipp and élet > 0:
    tipp = int(input('Tippelj: '))
    if tipp == a :
        print('Nyertél')
        
    elif a > tipp:
        print('A gondolt szám nagyobb')
        élet-=1
        print(f'{élet} tipped maradt')
    
    else:
        print('A gondolt szám kisebb')
        élet-=1
        print(f'{élet} tipped maradt')
    
if élet == 0:
        print('vesztettél')
         