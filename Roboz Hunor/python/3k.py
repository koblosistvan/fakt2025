a = int(input('Adj meg egy számot ' ))
prim = False
for i in range (2,a//2+1):
    if a % i == 0:
        prim = False
    else:
        prim = True
if prim == True:
    print('Prím')
else:
    print('Nem prím')
    