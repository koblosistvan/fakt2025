forras = open('Dobai Balint\\python\\5a-magasugras2.txt', mode = 'r', encoding= 'utf-8')

tavaly = []
iden = []

for sor in forras:
    adat = sor.strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close()
versenyzok_szama = len(tavaly)

legmagasabb = tavaly[0]
legmagasabb_index = 0

for i in range(versenyzok_szama):
    if tavaly[i] > legmagasabb:
        legmagasabb = tavaly[i]
        legmagasabb_index = i+1
print(f'a legmagasabb ugras {legmagasabb} melyet a {legmagasabb_index}. ember ugrott' )


legalacsonyabb = tavaly[0]
legalacsonyabb_index = 0 
for i in range(1, versenyzok_szama):
    if tavaly[i] < legalacsonyabb:
        legalacsonyabb = tavaly[i]
        legalacsonyabb_index = i+1

print(f' a legkisebb ugras {legalacsonyabb}, melyet a {legalacsonyabb_index}. versenyzo ugrott')


legnagyobb_fejlodes = iden[0] - tavaly[0]
legnagyobb_fejlodes_index = 0
legnagyobb_eses = iden[0] - tavaly[0]
legnagyobb_eses_index = 0
for i in range(versenyzok_szama):
    if legnagyobb_fejlodes < iden[i]- tavaly[i]:
        legnagyobb_fejlodes_index = i
        legnagyobb_fejlodes = iden[i]-tavaly[i]
    if legnagyobb_eses > iden[i]- tavaly[i]:
        legnagyobb_eses_index = i
print(f' a legnagyobb fejlodes {legnagyobb_fejlodes} cm, melyet {legnagyobb_fejlodes_index} erte el')
print(f' a legnagyobb fejlodes {legnagyobb_eses} cm, melyet {legnagyobb_eses_index} erte el')














#for i in range(versenyzok_szama):
 #   if szam_felett > 180:
 #       szam_felett_index = i
  #      szam_felett