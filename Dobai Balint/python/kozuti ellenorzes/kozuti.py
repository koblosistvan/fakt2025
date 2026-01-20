forras = open('Dobai Balint\\kozuti ellenorzes\\kozut.txt', mode ='r', encoding='utf-8')
forras.readline()
ora, perc, masdodp , sebesseg , rendszam = [] , [] , [] , [], []

for sor in forras:
    adat = sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    masdodp.append(int(adat[2]))
    sebesseg.append(int(adat[3]))
    rendszam.append(str(adat[4]))
forras.close

def f(n):
    print(f'\n {n}. feladat')

f(1)
max_felett = 0
for i in range(len(sebesseg)):
    if sebesseg[i] > 50:
        max_felett +=1
print(f'{max_felett} auto haladt az 50es megengedettnel gyorsabban')

f(2)

for i in range(len(sebesseg)):
    if sebesseg[i] > 55:
        print('Volt olyan auto ami 55-nel tobbel ment')
        break
    else:
        print('Nem ment auto 55-nel gyorsabban')

f(3)
leggyorsabb = sebesseg[0]
leggyorsabb_rendszam = rendszam[0]
for i in range(len(sebesseg)):
    if sebesseg[i] > leggyorsabb:
        leggyorsabb = sebesseg[i]
        leggyorsabb_rendszam = rendszam[i]
print(f'A leggyorsabb auto rendszama {leggyorsabb_rendszam} es {leggyorsabb} km/h-val ment')

f(4)
print(f'A sebessegek atlaga: {sum(sebesseg) / len(sebesseg):.2f}')

f(5)
harminc_alatt = []
for i in range(len(sebesseg)):
    if sebesseg[i] < 30:
        harminc_alatt.append(ora[i])
        harminc_alatt.append(perc[i])
        harminc_alatt.append(masdodp[i])
        harminc_alatt.append(rendszam[i])
        harminc_alatt.append(sebesseg[i])
elso = harminc_alatt[:5]
masodik = harminc_alatt[5:10]
harmadik = harminc_alatt[10:15]
print(f'Az elso ilyen auto adatai: {elso}')
print(f'Az masodik ilyen auto adatai: {masodik}')
print(f'Az harmadik ilyen auto adatai: {harmadik}')

f(7)
for i in range(len(sebesseg)-1):
    if sebesseg[i] > 90 and sebesseg[i+1] > 90:
        print('Volt utcai vereseny')
        break
    else:
        print('Nem tortent ilyen')
        break
'''
f(8)
elhaladott = []
for i in range(len(rendszam)):
    if rendszam[i] not in elhaladott:
        elhaladott.append(rendszam[i])
'''




    
