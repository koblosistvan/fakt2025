a= float(input('a = '))
b= float(input('b = '))
c= float(input('c = '))
D=b**2 -4*a*c

if D < 0:
    print('nincs megoldás')
elif D==0:
    print(f'Csak egy megoldás van és az: {}')

else:
    print(f'x1 = {(-b + D**0.5)/(2*a)} x2 = {-b - D**0.5/(2*a)}')