# 1. feladat: mit ír ki?
a = int(input('Mondj egy számot: '))
for i in range(1, a+1):
    print(i**2)

''' 
- 1 és a közötti számok
- négyzetét kiírja 
'''

# 2. feladat: hol a hiba?
# A program feladata, hogy kiírja a megadott szám osztóit
szám = int(input('Add meg a számot: '))
if szám < 1:
    print('Nincs pozitív osztója.')
else:
    for i in range(1, szám+1):
        if szám % i == 0:
            print(i)

'''
- szám-ot int-re kell konvertálni
- print-nél nincs bezárva a zárójel
- range szám+1-ig
- if-ben dupla =
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
- megszámolja, hogy hány b-nél nagyobb szám van a listában 
- a: adatok
- b: az értékhatár
- c: számláló
'''
