forras = open('_Megoldások\\python\\5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly = []
iden = []
for sor in forras:
    adat = sor.strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close()
versenyzok_szama = len(tavaly)

legmagasabb = tavaly[0]         # azt feltételezem, hogy a 0. a legmagasabb
legmagasabb_index = 0

for i in range(1, versenyzok_szama):
    if tavaly[i] > legmagasabb:
        legmagasabb = tavaly[i]
        legmagasabb_index = i

print(f'A legmagasabb ugrás {legmagasabb} cm volt, melyet a {legmagasabb_index+1}. versenyző ugrott.')


legalacsonyabb = tavaly[0]         
legalacsonyabb_index = 0

for i in range(1, versenyzok_szama):
    if tavaly[i] < legalacsonyabb:
        legalacsonyabb = tavaly[i]
        legalacsonyabb_index = i

print(f'A legalacsonyabb ugrás {legalacsonyabb} cm volt, melyet a {legalacsonyabb_index+1}. versenyző ugrott.')
print(f'A legalacsonyabb ugrás {min(tavaly)} cm volt, melyet a {tavaly.index(min(tavaly))}. versenyző ugrott.')


legnagyobb_fejlodes_index = 0
legnagyobb_fejlodes = iden[0] - tavaly[0]
for i in range(versenyzok_szama):
    if legnagyobb_fejlodes < iden[i] - tavaly[i]:
        legnagyobb_fejlodes_index = i
        legnagyobb_fejlodes = iden[i] - tavaly[i]
print(f'A legnagyobb fejlődést a {legnagyobb_fejlodes_index+1}. versenyző érte el, {tavaly[legnagyobb_fejlodes_index]} => {iden[legnagyobb_fejlodes_index]}, azaz {legnagyobb_fejlodes} cm.')
