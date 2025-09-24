szam = int(input("Adj meg egy számot: "))

prim = True
for i in range(2, szam // 2 + 1):
    if szam % i == 0:
        prim = False
    
if szam == 1:
    print('Az 1 nem prím')    
elif prim:
    print(f'{szam} egy prímszám.')
else:
    print(f'{szam} nem prímszám.')