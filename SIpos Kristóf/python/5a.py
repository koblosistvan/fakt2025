forras=open('Sipos Kristóf\\python\\5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly= []
iden = []
for sor in forras:
    adat= sor.strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close()
versenyzok_szama=len(tavaly)

legmagasabb= tavaly [0]
legmagasabb_index=0
for i in range(1, versenyzok_szama):
    if tavaly [i] > legmagasabb:
        legmagasabb = tavaly[i]
        legmagasabb_index = i

legalacsonyabb = tavaly [0]
legalacsonyabb_index= 0
for i in range(1, versenyzok_szama):
    if tavaly [i] < legalacsonyabb:
        legalacsonyabb = tavaly[i]
        legalacsonyabb_index= i
print(f'A legmagasabb ugrás {legmagasabb}cm volt és a {legmagasabb_index+1}. versenyző ugrotta.')
print(f'A legalacsonyabb ugrás {legalacsonyabb}cm volt és a {legalacsonyabb_index+1}. versenyző ugrotta.')

legnagyobb_rontas= iden[0] - tavaly[0]
legnagyobb_rontas_index = 0
legnagyobb_fejlodes = iden[0] - tavaly[0]
legnagyobb_fejlodes_index=0
for i in range(versenyzok_szama):
    if legnagyobb_fejlodes < iden[i]- tavaly[i]:
        legnagyobb_fejlodes_index=i
        legnagyobb_fejlodes = iden[i]-tavaly[i]
    if legnagyobb_rontas > iden[i] - tavaly[i]:
        legnagyobb_rontas_index=i
        legnagyobb_rontas = iden[i]-tavaly[i]
        
print(f'A legnagyobb fejlődés {legnagyobb_fejlodes} cm-rel volt a {legnagyobb_fejlodes_index+1} versenyző volt.')
print(f'A legnagyobb fejlődés {legnagyobb_rontas} cm-rel volt a {legnagyobb_rontas_index+1} versenyző volt.')
