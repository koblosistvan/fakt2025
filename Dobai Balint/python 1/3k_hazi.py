szam = int(input('adj meg egy szamot'))

if szam < 2:
    print(f'{szam} nem primszam')

else: 
    prim = True
    for i in range(2, int(szam**0.5)+1):
        if szam % i == 0:
            prim = False
            break

if prim:
    print(f'a {szam} primszam')
else:
    print(f'a {szam} nem primszam')