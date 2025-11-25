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
    pont.append(adat[3])
    pont_kulonb.append(adat[4])
    eredmeny.append(adat[5])
forras_cs.close()

print(f'Összesen {len(ido)/2:.0f} meccseredményem van.')
print(f'Az első meccs {min(ido)}-kor volt')