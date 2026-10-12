forras = open('Szmodis Vince\\Erettsegi\\2024 okt\\progarmozas\\uvegek.txt', mode='r', encoding='utf-8')
sor = forras.readline()
data  = sor.strip().split(',')
adat = []
for i in range(15):
    adat.append(int(data[i]))

print('2. feladat')

L = int(input('Mari néni lekvárja (dl): '))
if L>200 or L<0: 
    L=0

print('3. feladat')
max=adat[0]
max_index=0
for i in range(len(adat)-1):
    if max<adat[i]:
        max=adat[i]
        max_index=i
print(f'A legnagyobb üveg: {max} dl és {max_index}. a sorban. ')

print('4. feladat ')
ossz = 0
for i in range (len(adat)):
    ossz+=adat[i]


if ossz>L:
    print('Elegendő üveg volt.')
else:
    
    print('Maradt lekvár.')