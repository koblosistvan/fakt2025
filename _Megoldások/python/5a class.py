class Eredmeny:
    tavaly: int
    iden: int

forras = open('_Megoldások\\python\\5a-magasugras2.txt', mode='r', encoding='utf-8')

adatok = []
for sor in forras:
    adat = sor.strip().split(';')
    e = Eredmeny()
    e.tavaly = int(adat[0])
    e.iden = int(adat[1])
    adatok.append(e)
forras.close()
versenyzok_szama = len(adatok)

legmagasabb = min(adatok, key=tavaly).tavaly
legmagasabb_index = 0

for i in range(1, versenyzok_szama):
    if adatok[i].tavaly > legmagasabb:
        legmagasabb = adatok[i].tavaly
        legmagasabb_index = i

print(f'A legmagasabb ugrás {legmagasabb} cm volt, melyet a {legmagasabb_index+1}. versenyző ugrott.')


legalacsonyabb = adatok[0].tavaly
legalacsonyabb_index = 0

for i in range(1, versenyzok_szama):
    if adatok[i].tavaly < legalacsonyabb:
        legalacsonyabb = adatok[i].tavaly
        legalacsonyabb_index = i

print(f'A legalacsonyabb ugrás {legalacsonyabb} cm volt, melyet a {legalacsonyabb_index+1}. versenyző ugrott.')


legnagyobb_fejlodes_index = 0
legnagyobb_fejlodes = adatok[0].iden - adatok[0].tavaly
for i in range(versenyzok_szama):
    if legnagyobb_fejlodes < adatok[i].iden - adatok[i].tavaly:
        legnagyobb_fejlodes_index = i
        legnagyobb_fejlodes = adatok[i].iden - adatok[i].tavaly
print(f'A legnagyobb fejlődést a {legnagyobb_fejlodes_index+1}. versenyző érte el, {adatok[legnagyobb_fejlodes_index].tavaly} => {adatok[legnagyobb_fejlodes_index].iden}, azaz {legnagyobb_fejlodes} cm.')
