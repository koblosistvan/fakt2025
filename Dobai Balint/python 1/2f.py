a = float(input('a ='))
b = float(input('b ='))
c=float(input('c ='))

d = b**2 - 4*a*c

if d < 0:
    print('nincs valos gyok')
elif d==0:
    print('egy valos gyok')
else:
    print(f'x1={(-b+d**0.5)/(2*a)}  x2={-(b+d**0.5)/(2*a)}') 
elif:
    print('egy van')