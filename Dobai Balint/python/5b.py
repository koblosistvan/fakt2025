forras = open('Dobai Balint\\python\\5b-homerseklet.txt.', mode = 'r', encoding = 'utf-8')

ido = []
homerseklet = []

for sor in forras:
    adat = sor.strip().split('\t')
    ido.append(adat[0])
    homerseklet.append(float(adat[1]))
forras.close()

meresek_szama =len(homerseklet)

harmicfelett = [0]
harmincfelett_index = 0


for i in range(meresek_szama):
    if homerseklet[i] > 30:
        harmincfelett = homerseklet[i]
        harmincfelett_index += 1
print(f'a harminc feletti meresek szama {harmincfelett_index}')

atlag = sum(homerseklet) / len(homerseklet)

print(f'{atlag:.2f} volt az atlaghomerseklet')


novekes = [0]
csokkenes = [0]
novekedes_index = 0
csokkenes_index = 0



for i in range(meresek_szama):
    if homerseklet[i] > homerseklet[i-1]:
        novekes = homerseklet[i]
        novekedes_index += 1
    if homerseklet[i] < homerseklet[i-1]:
        csokkenes = homerseklet[i]
        csokkenes_index += 1 

print(f'az elozo naphoz kepest {novekedes_index}-szer nott a homerseklet')
print(f'az elozo naphoz kepest {csokkenes_index}-szer csokkent a homerseklet')


legnagyobb = homerseklet[0]
legnagyobb_index = 0
legkisebb = homerseklet[0]
legkisebb_index = 0


for i in range(1, len(homerseklet)):
    if homerseklet[i] < legkisebb:
        legkisebb = homerseklet[i]
        legkisebb_index = i+1
    if homerseklet[i] > legnagyobb:
        legnagyobb = homerseklet[i]
        legnagyobb_index = i+2

ora1 = legkisebb_index //2 
perc1 = (legkisebb_index % 2)*30

ora2 = legnagyobb_index //2 
perc2 = (legnagyobb_index % 2)*30

print(f' a legkisebb mert ertek : {legkisebb}, {ora1:02d}:{perc2:02d}')
print(f' a legnagyobb mert ertek : {legnagyobb}, {ora2:02d}:{perc2:02d}-kor')

legn_emelkedes = homerseklet[1]-homerseklet[0]
emel1 = 0                                                 
emel2 = 0

for i in range(1, len(homerseklet)):
    emelkedes = homerseklet[i] - homerseklet[i-1]
    if emelkedes > legn_emelkedes:
        legn_emelkedes = emelkedes
        emel1 = i-1
        emel2 = i





print(f'a legnagyobb emelkedes {legn_emelkedes:.1f} volt {emel1} es {emel2} kozott')


    
        


    
