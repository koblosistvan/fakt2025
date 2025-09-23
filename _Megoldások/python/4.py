p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(p)
print(p[1])
print(f'Az első érték: {p[0]}')

print(f'Az utolsó érték: {p[-1]}')

print(p[1:3])
print(p[1:])
print(p[:3])

print(p[1:5:2])

szöveg = 'Még nyílnak a völgyben a kerti virágok...'
print(szöveg)
print(szöveg[0:5])
print(szöveg[::-1])

if 11 in p:
    print('Benne van.')
else:
    print('Nincs benne')