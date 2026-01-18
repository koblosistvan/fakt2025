# 1. feladat: mit ír ki?
a = int(input('Mondj egy számot: '))
for i in range(1, a+1):
    print(i**2)

''' 
ide írd a megoldást
'''

# 2. feladat: hol a hiba?
# A program feladata, hogy kiírja a megadott szám osztóit
szám = input('Add meg a számot: ')
if szám < 1:
    print 'Nincs pozitív osztója.'
else:
    for i in range(1, szám):
        if szám % i = 0:
            print(i)

'''
-
-
-
-
'''

# 3. feladat: mit csinál, mi a változók feladata?
a = [2, 6, 3, 5, 8, 1, 3, 7]
b = 3
c = 0
for i in range(len(a)):
    if a[i] > b:
        c += 1
print(c)

'''
- cél: 
- a: 
- b: 
- c: 
'''
