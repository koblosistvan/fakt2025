p=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(p)
print(p[1])

print(f'Az első érték {p[0]}')

print(p[1:3])

print(p[1:])
print(p[:3])


szöveg= 'Még nyílnak a völgyben a kerti virágok'

print(szöveg[0:6])
print(szöveg[::-1])

if 11 in p:
    print('Benne van')

else:
    print('Nincs benne')