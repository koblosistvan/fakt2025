import random
lotto = []
for i in range(5):
    lotto.append(random.randint(1,91))

print(lotto)

tippek = []
for i in range(5):
    tippek.append(int(input('adj meg egy szamot : ')))

tipp_szam = 0

for i in range(len(lotto)):
    if lotto[i] == tippek[i]:
        tipp_szam = i+1
        print(f' {tipp_szam} db helyes tipped volt')
    else:
        print('0 helyes tipped van')
        break
