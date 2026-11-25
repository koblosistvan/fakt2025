forras = open('Dobai Balint\\python 1\\6a-hallgatok.txt', mode = 'r', encoding='utf-8')
forras.readline()
class Hallgato:

    szul_ev = int
    szul_honap = int
    szul_nap = int
    kezdes_eve = int
    vegzes_eve = int

    def __init__(self,sor):
        adat = sor.strip().split()
        self.szul_ev = int(adat[0])
        self.szul_honap = int(adat[1])
        self.szul_nap = int(adat[2])
        self.kezdes_eve = int(adat[3])
        self.vegzes_eve = int(adat[4])

        self.diploma_kor = self.vegzes_eve - self.szul_ev
        self.szulinap = f'{self.szul_honap}.{self.szul_nap}'
        self.szuletesi_ido = f'{self.szul_ev}.{self.szul_honap}.{self.szul_nap}'
        self.eletkor =  2014 - self.szul_ev

    def __repr__(self):
        return f'{self.szul_ev}.{self.szul_honap}. {self.szul_nap} {self.kezdes_eve}-{self.vegzes_eve}'

hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))

#1 feladat

kor = int(input('add meg az életkort:'))

for hallgato in hallgatok:
    if hallgato.diploma_kor < kor:
        print('Van ennél fiatalabban végzett hallgató')
        break
else:
    print('Nincs ennél fiatalabban végzett hallgató')

#2 feladat

szulinap = '12.22'
for hallgato in hallgatok:
    if hallgato.szulinap == szulinap:
        print('Van olyan akinek azonos a szülinapja')
        break
else:
    print('nincs olyan')


#3 feladat

legfiatalabb = hallgatok[0]
for hallgato in hallgatok:
    if hallgato.diploma_kor < legfiatalabb.diploma_kor:
        legfiatalabb = hallgato
print(f'a legfiatalabban végzett hallgató  születési dátuma {legfiatalabb.szuletesi_ido}')

#4 feladat
akkor_vegzett = 0

for hallgato in hallgatok:
    if hallgato.vegzes_eve == 2016:
        akkor_vegzett +=1
print(f'2016-ban {akkor_vegzett} ember végzett')

#5 feladat
osszeg = 0 
diakok = len(hallgatok)
for hallgato in hallgatok:
    osszeg += hallgato.eletkor
    

atlag = osszeg / diakok

print(f'Az átlagéletkor {atlag}')





