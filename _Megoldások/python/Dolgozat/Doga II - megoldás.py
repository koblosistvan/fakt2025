# 1. feladat: mit ír ki?
a = 17
while a/5 != a//5:
    print(a, end=',')
    a -= 1
print()

''' 
- 17, 16, 
- ,-vel elválasztva
'''

# 2. feladat: hol a hiba?
# A program feladata, hogy megszámolja egy szóban a magánhangzókat
magánhangzók = "aáeéiíoóöőuúüű"
szöveg = input('Adj meg egy tetszőleges szöveget: ')
darab = 0
for c in szöveg:
    if c in magánhangzók:
        darab += 1
print(f'A szövegben {darab} magánhangzó van.')

'''
- a szöveget nem kell int-re konvertálni
- if végén kell :
- darab-ot inicializálni kell
- f sztringben {} kell a darab köré
- darab-ot kell inkrementálni, nem c-t
'''

# 3. feladat: mit csinál, mi a változók feladata?
a = "indul a görög aludni"
b = len(a)
for i in range(len(a)):
    print(a[b-i-1], end='')
print()

'''
- cél: a megadott szöveget visszafelé írja ki
- a: szöveg
- b: a szöveg hossza
'''
