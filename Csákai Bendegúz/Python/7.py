forras = open('fakt2025\\Csákai Bendegúz\\Python\\7a-lakas-arak.txt', mode='r', encoding='utf-8')
forras.readline()
terulet = []
ar = []
for sor in forras:
    adat = sor.strip().split(' ')
    terulet.append(int(adat[0]))
    ar.append(int(adat[1]))
forras.close()

kerter = len(terulet)

legd_lak=ar[0]
legd_lak_index=0
for i in range(kerter):
    if ar[i] > legd_lak:
        legd_lak = ar[i]
        legd_lak_index = i
print(f'A legdrágább lakás {legd_lak} millió forint, a {legd_lak_index}. sorban található')

for i in range(kerter):
    if ar[i] > 500:
        print('Van 500 milliónál drágább ház')
        break
else:
    print('Nincs 500 milliónál drágább ház')

terperar = ar[0] / terulet[0]
terperar_i = 0
for i in range(kerter):
    if ar[i] / terulet[i] > terperar:
        terperar = ar[i] / terulet[i]
        terperar_i = i
print(f'A legnagyobb négyzetméterárú ház a {terperar_i}.')

huszalatti = 0
for i in range(kerter):
    if ar[i] < 20:
        huszalatti += 1
print(f'{huszalatti} db ház van 20M alatt')

kimenet = open('fakt2025\\Csákai Bendegúz\\Python\\arak.txt', mode='w', encoding='utf-8')



for i in range(kerter):
    if 50 <= terulet[i] <= 60:
        print(f'{terulet[i]}NM - {ar[i]} millió', file=kimenet)
kimenet.close()
    