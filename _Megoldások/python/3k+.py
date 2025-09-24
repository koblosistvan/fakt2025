print('Prímek 100-ig:')
for szam in range(2, 101):
    prim = True
    for i in range(2, szam // 2 + 1):
        if szam % i == 0:
            prim = False
        
    if prim:
        print(f'{szam}')
