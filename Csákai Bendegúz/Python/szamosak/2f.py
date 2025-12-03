a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4*a*c
if d < 0:
    print('Nincs megoldás')
elif d == 0:
    print(f'x1 = {(-b + d**0.5)/(2*a)}')
else:
    print(f'x1 = {(-b + d**0.5)/(2*a)}')
    print(f'x2 = {(-b - d**0.5)/(2*a)}')
