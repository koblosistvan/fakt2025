a = int(input('Adj meg egy testzőleges számot: '))
b = int(input('Adj meg egy másik számot'))

if a > b and a % b == 0:
    print(f'A 2 szám osztható egymással, és az eredmény {a/b}')
elif b > a and b % a == 0:
    print(f'A 2 szám osztható egymással, és az eredmény {b/a}')
else:
    print('A 2 szám nem osztható egymással')
