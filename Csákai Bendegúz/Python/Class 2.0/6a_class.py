import os
os.system('cls')

forras = open('fakt2025\\Csákai Bendegúz\\Python\\szamosak\\6a-hallgatok.txt', mode= 'r', encoding= 'utf-8')
forras.readline()

class Hallgato:
    born_year: int
    born_month: int
    born_day: int
    first_year: int
    last_year: int

    def __init__(self, sor):
        adat = sor.strip().split()
        self.born_year = int(adat[0])
        self.born_month = int(adat[1])
        self.born_day = int(adat[2])
        self.first_year = int(adat[3])
        self.last_year = int(adat[4])
        self.diplomakor = self.last_year-self.born_year
        self.birthday = f'{self.born_month}.{self.born_day}'
        self.born_full = f'{self.born_year}.{self.born_month:0>2d}.{self.born_day:0>2d}'
    def __repr__(self):
        return f'{self.born_year}.{self.born_month:0>2d}.{self.born_day:0>2d} /{self.first_year}-{self.last_year}/'
hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))
print('Vége a beolvasásnak.')

'''# 1.Feladat
kor = int(input('Adj meg egy életkort: '))
for hallgato in hallgatok:
    if hallgato.diplomakor < kor:
        print('Van ennél fiatalabban végzett hallgató.')
        break
else:
    print('Nincs ennél fiatalabban végzett hallgató.')
akikretelj_szam = sum([1 for h in hallgatok if h.diplomakor < kor])
print(akikretelj_szam)

# 2.feladat

teszul = input('Add meg mikor van a szülinapod (ponttal elválasztva):')
for hallgato in hallgatok:
    if hallgato.birthday == teszul:
        print('Van veled egy napon született hallgató.')
        break
else:
    print('Nincs veled egy napon született hallgató.')

# 3.feladat

legf = hallgatok[0]
for i in range(len(hallgatok)):
    if hallgatok[i].diplomakor < legf.diplomakor:
        legf = hallgatok[i]

print(f'A legfiatalabban vizsgázott hallgató születésiu ideje: {legf.born_full}')

 #4.feladat

veg_2016 = sum([1 for h in hallgatok if h.last_year == 2016])

print(veg_2016)

'''# 5.feladat

korok = []
db = 0
for h in hallgatok:
    if h.birthday > '05.07':
        korok.append()
atl_kor = sum(korok)/db

print(atl_kor)

