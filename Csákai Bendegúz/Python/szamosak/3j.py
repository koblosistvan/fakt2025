szam = int(input('Adj meg egy számot: '))
alap = int(input('Add meg melyik számrendszerben (1 = kettes, 2 = 16-os): '))
a = szam
eredmeny = ''
if alap == 1:
    while szam > 0:
        maradek = szam % 2
        eredmeny = str(maradek) + eredmeny
        szam = (szam-maradek) // 2
    print(f'{a} kettes számrendszerben: {eredmeny}')
elif alap == 2:
    while szam > 0:
        maradek = szam % 16
        eredmeny = str(maradek) + eredmeny
        szam = (szam-maradek) // 16
    print(f'{a} tizenhatos számrendszerben: {eredmeny}')