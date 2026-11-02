adatok = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]

def f(n):
    print(f'\n{n}. feladat \n')

f(2)
l = int(input())
print(f'Mari néni lekvárja (dl): {l}.')

f(3)
legn_ind = 0
legn = adatok[0]
for i in range(len(adatok)):
    if adatok [i] > legn:
        legn = adatok[i]
        legn_ind = i+1
print(f'A legnagyobb üveg: {legn} dl és a {legn_ind}. a sorban.')

f(4)
if sum(adatok) >= l:
    print('Elegendő üveg volt.\n')
else:
    print('Maradt lekvár.\n')