a = int(input('Adj meg egy számot: '))
prim = True
while prim == True:
    if a % 2 == 0:
        prim = False
    else:
        print('A szám prím')
    