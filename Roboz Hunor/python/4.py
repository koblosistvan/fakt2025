p = [1,2,3,4,5,6,7,8,9,10]

print(p)
print(p[1])
print(f' az első érték {p[0]}')
print(f' az utolsó érték {p[-1]}')

print(p[1:3]) 
print(p[1:])
print(p[:3])

print(p[1:6:2]) #hányasával

szöveg = 'Még nyílnak a kertben a kerti virágok'
print(szöveg[0:6])
print(szöveg[::-1]) #visszafelé

if 5 in p:
    print('Benne van')
else:
    print('nincs benne')

