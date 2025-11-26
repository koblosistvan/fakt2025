forras_cs = open('fakt2025\\Csákai Bendegúz\\Python\\CS\\cs.csv', mode='r', encoding='utf-8')
forras_mr = open('fakt2025\\Csákai Bendegúz\\Python\\CS\\match_results.csv', mode='r', encoding='utf-8')
forras_cs.readline()
forras_mr.readline()
ido = []
map = []
team = []
pont = []
pont_kulonb = []
eredmeny = []
for sor in forras_cs:
    adat = sor.strip().split(';')
    ido.append(adat[0])
    map.append(adat[1])
    team.append(adat[2])
    pont.append(int(adat[3]))
    pont_kulonb.append(int(adat[4]))
    eredmeny.append(adat[5])
forras_cs.close()

print(f'Összesen {len(ido)/2:.0f} meccseredményem van.')
print(f'Az első meccs {min(ido)}-kor volt')

for i in range(len(ido)):
    for j in range(len(ido)-i-1):
        if pont_kulonb[j] < pont_kulonb[j+1]:
            pont_kulonb[j], pont_kulonb[j+1] = pont_kulonb[j+1], pont_kulonb[j]
            ido[j], ido[j+1] = ido[j+1], ido[j]
            map[j], map[j+1] = map[j+1], map[j]
            team[j], team[j+1] = team[j+1], team[j]
            pont[j], pont[j+1] = pont[j+1], pont[j]
            eredmeny[j], eredmeny[j+1] = eredmeny[j+1], eredmeny[j]
map_szam = []
for i in range(len(map)):
    if map[i] not in map_szam:
        map_szam.append(map[i])
print(f'Összesen {len(map_szam)} pályán játszottak.')

extra_salt_meccs = 0
for i in range(len(team)):
    if team[i] == 'Extra Salt':
        extra_salt_meccs+=1
print(f'Az Extra Salt csapat összesen {extra_salt_meccs} meccset játszott.')

veres = 0
dont = 0
nyert = 0
for i in range(len(eredmeny)):
    if team[i] == 'Extra Salt' and eredmeny[i] == 'vereség':
        veres +=1
    elif team[i] == 'Extra Salt' and eredmeny[i] == 'döntetlen':
        dont +=1
    elif team[i] == 'Extra Salt' and eredmeny[i] == 'győzelem':
        nyert +=1
print(f'Ezekből a meccsekből {nyert} győzelem lett, {veres} vereség lett, valamint {dont} döntetlent játszottak.')

es_kul = []
for i in range(len(pont_kulonb)):
    if team[i] == 'Extra Salt':
        es_kul.append(pont_kulonb[i])
print(f'A legnagyobb pontkülönbség {max(es_kul)}, a legkisebb {min(es_kul)} volt.')
print(f'A pontkülönbségek átlaga: {sum(es_kul)/len(es_kul)}')

kimenet=open('fakt2025\\Csákai Bendegúz\\Python\\CS\\Top 10.txt', mode='w', encoding='utf-8')

i = 0
n = len(ido)
while i < n-1:
    if pont_kulonb[i] <= pont_kulonb[i+1]:
        i +=1
    else:
        pont_kulonb[i], pont_kulonb[i+1] = pont_kulonb[i+1], pont_kulonb[i]
        ido[i], ido[i+1] = ido[i+1], ido[i]
        map[i], map[i+1] = map[i+1], map[i]
        team[i], team[i+1] = team[i+1], team[i]
        pont[i], pont[i+1] = pont[i+1], pont[i]
        eredmeny[i], eredmeny[i+1] = eredmeny[i+1], eredmeny[i]
        if i > 0:
            i -= 1