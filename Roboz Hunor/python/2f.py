a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2-4*a*c

if d < 0:
    print('nincs megoldás')
elif d ==0:
    print(f'{(-b + d ** 0.5) /2 * a}')
else:
    print(f'{(-b + d ** 0.5) /2 * a}')
    print(f'{(-b - d ** 0.5) /2 * a}')