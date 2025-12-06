a = input().split()

b = int(a[0])
c = int(a[1])
d = int(a[2])
e = int(a[3])
if (b+c == d+e 
    or b+d == c+e 
    or b+e == c+d
    or b+c+d == e
    or b+c+e == d
    or b+e+d == c
    or c+d+e == b):
    print('IGEN')
else: print('NEM')

