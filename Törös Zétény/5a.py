forras = open('Törös Zétény\\5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly= []
iden= []

for sor in forras:
    adat = sor.strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close()

print(tavaly)

legmagasabb = tavaly[0]
legmagasabb_index = 0
versenyzok_szama = len(tavaly)

for i in range(versenyzok_szama):
    if tavaly [i] > legmagasabb:
        legmagasabb = tavaly[i]
        legmagasabb_index = i
print(f'A legmagasabb ugrás {legmagasabb}cm volt és a {legmagasabb_index+1}. versenyző ugrotta')

legalacsonyabb = tavaly [0]
legalacsonyabb_index = 0
for i in range(versenyzok_szama):
    if tavaly [i] < legalacsonyabb:
        legalacsonyabb = tavaly[i]
        legalacsonyabb_index = i
print(f'A legalacsonyabb ugrás {legalacsonyabb}cm volt és a {legalacsonyabb_index+1}. versenyző ugrotta.')

legnagyobb_romlás = tavaly[0] - iden [0]
legnagyobb_romlás_index = 0

legnagyobb_fejlodes_index = 0
legnagyobb_fejlodes= iden [0] - tavaly[0]
for i in  range(versenyzok_szama):  
    if legnagyobb_fejlodes < iden [i] - tavaly[i]:
        legnagyobb_fejlodes_index = i
        legnagyobb_fejlodes = iden[i] - tavaly[i]
