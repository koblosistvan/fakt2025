forras = open('Dobai Balint\\python\\7a-lakas-arak.txt', mode ='r', encoding='utf-8')
lakasok_szama = int(forras.readline())

terulet =[]
ara = []

for sor in forras:
    adat = sor.strip().split(' ')
  
    terulet.append(int(adat[0]))
    ara.append(int(adat[1]))
forras.close()

legdragabb = ara[0]
legdragabb_index = 0

for i in range(lakasok_szama):
    if ara[i] > legdragabb:
        legdragabb = ara[i]
        legdragabb_index = i+1
print(f'a legdragabb lakas a {legdragabb_index}-edik, {legdragabb} millio forintert')


otszaz_felett = ara[0]

for i in range(lakasok_szama):
    if ara[i] > 500:
        ara[i] = otszaz_felett
        print('van 500 millio forint feletti lakas')
else: print(f'nincs 500 millio forint feletti lakas')

arertek = ara[0] / terulet[0]
arertek_index = 0

for i in range(lakasok_szama):
    if ara[i] / terulet[i] > arertek:
        arertek = ara[i] / terulet[i]
        arertek_index = i+1
print(f'a legjobb arertek aranya a {arertek_index}-edik lakasnak van')

husz_alatt = ara[0]
husz_alatt_index = 0


for i in range(lakasok_szama):
    if ara[i] < 20:
        ara[i] = husz_alatt
        husz_alatt_index +=1

print(f'{husz_alatt_index} lakas van ami 20 millio forint alatt van')


