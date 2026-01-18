import random
letsz = random.randint(15,20)
oszt = []
for i in range(letsz):
    oszt.append(random.randint(1,5))
print(oszt)
print(f'Az osztályzatok száma: {letsz}')
print(f'Az osztályzatok összege: {sum(oszt)}')
print(f'Az osztályzatok átlaga: {sum(oszt)/letsz:.1f}')
for i in range(letsz):
    if oszt[i] == 1:
        print('Van 1-es osztályzat.')
        break
else:
    print('Nincs 1-es osztályzat.')
jegy = int(input('Melyik jegyet szeretnéd ellenőrizni?: '))
jegy_i = 0
for i in range(letsz):
    if oszt[i]==jegy:
        jegy_i = i+1
        print(f'Az osztályzatok között a {jegy}-es/as/ös {jegy_i}. helyen fordul elő először.')
        break
else:
    print(f'Az osztályzatok között nincsen {jegy}-es/as/ös.')
for i in range(letsz):
    if oszt[i] == jegy:
        jegy_i = i+1
        print(f'{jegy}-as/-es/-ös {jegy_i} helyen van.')
ketto_szama=0
for i in range(letsz):
    if oszt[i] == 2:
        ketto_szama+=1
print(f'A 2-es osztályzat {ketto_szama}x fordul elő')
koz_jobb = 0
for i in range(letsz):
    if oszt[i] > 3:
        koz_jobb+=1
print(f'A közepesnél jobb osztályzatok száma: {koz_jobb}')
print(f'Ezek százalékos aránya: {koz_jobb/letsz*100:.2f}')
print(f'A legkisebb osztályzat: {min(oszt)}')
print(f'A legnagyobb osztályzat: {max(oszt)}')