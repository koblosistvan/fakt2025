forras = open('_Feladatok\\python\\5a-magasugras2.txt', mode = 'r', encoding = 'utf-8')

tavaly=[]
iden=[]
for sor in forras:
    adat = sor.strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close()

versenyzok_szama = len(tavaly)
legm = tavaly[0]
legm_index = 0
for i in range(1, versenyzok_szama):
    if tavaly[i] > legm:
        legm = tavaly[i]
        legm_index = i
print(f'A legmagasabb ugrás {legm} cm volt amit a {legm_index+1}. versenyző ugrott')

lega = tavaly [0]
lega_index = 0
for i in range(1, versenyzok_szama):
    if tavaly[i] < lega:
        lega = tavaly[i]
        lega_index = i
print(f'A legalacsonyabb ugrás {lega} cm volt amit a {lega_index+1}. versenyző ugrott')

legn_fejl = 0
legn_fejl_index = iden[0]-tavaly[0]
legn_ront = 0
legn_ront_index = tavaly[0]-iden[0]
for i in range(versenyzok_szama):
    if legn_fejl < iden[i] - tavaly[i]:
        legn_fejl_index = i
        legn_fejl = iden[i] - tavaly[i]
    if legn_ront < tavaly[i]-iden[i]:
        legn_ront_index = i
        legn_ront = tavaly[i]-iden[i]
print(f'A legnagyobb fejlődést a(z) {legn_fejl_index+1}. versenyző érte el, aki {legn_fejl} cm-t javított')
print(f'A legnagyobb rontást a(z) {legn_ront_index+1}. versenyző érte el, aki {legn_ront} cm-t rontott')
