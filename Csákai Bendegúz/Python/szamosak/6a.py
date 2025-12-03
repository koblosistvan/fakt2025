forras = open('Csákai Bendegúz\\Python\\6a-hallgatok.txt', mode= 'r', encoding= 'utf-8')
born_year = []
born_month = []
born_day = []
kezdes_eve = []
vegzes_eve = []

adt_szm = int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    born_year.append(int(adat[0]))
    born_month.append(int(adat[1]))
    born_day.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor = int(input('Add meg az életkorodat: '))
for i in range(adt_szm):
    kor = vegzes_eve[i]-born_year[i]
    if kor < eletkor:
        print(f'Van {eletkor} évnél fiatalabb végzett')
        break
else:
    print(f'Nincs {eletkor} évnél fiatalabb végzett')

szul_ho = int(input('Add meg hányadik hónapban születtél: '))
szul_nap = int(input('Add meg hányadikán születtél: '))
for i in range(adt_szm):
    if born_month[i] - szul_ho == 0 and born_day[i] - szul_nap == 0:
        print(f'Van veled ugyan akkor, azaz {szul_ho}. {szul_nap}.-kor született ember')
        break
else:
    print(f'Nincs veled ugyan akkor, azaz {szul_ho}. {szul_nap}.-kor született ember')

legf_vegz = vegzes_eve[0] - born_year[0] #('*365 + 6*31 + 30')('*365 + born_month[0]*31 + born_day[0]')
legf_vegz_index = 0
for i in range(adt_szm):
    if legf_vegz > vegzes_eve[i]-born_year[i]:
        legf_vegz = vegzes_eve[i]-born_year[i]
        legf_vegz_index = i
print(f'A legfiatalabban végzett a {legf_vegz_index+1}. hallgató, aki {legf_vegz} évesen végzett, a {vegzes_eve[legf_vegz_index]}. évben.')

db_vegz_2016 = 0
for i in range(adt_szm):
    if vegzes_eve[i] == 2016:
        db_vegz_2016 += 1
print(f'{db_vegz_2016} db tanuló végzett 2016-ban.')

ossz_kor = 0
tan_ossz = 0
for i in range(adt_szm):
    if vegzes_eve[i] >= 2014 and kezdes_eve[i] <= 2016:
        ossz_kor += 2014-born_year[i]
        tan_ossz += 1
print(f'{tan_ossz} tanu')