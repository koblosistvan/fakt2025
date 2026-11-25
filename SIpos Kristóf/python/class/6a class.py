forras=open('Sipos Kristóf\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
forras.readline()
class Hallgato:
    szul_ev: int
    szul_ho: int
    szul_nap: int
    kezdes_eve: int 
    vegzes_eve: int

    def __init__(self, sor):
        adat = sor.strip().split()

        self.szul_ev = int(adat[0])
        self.szul_ho = int(adat[1])
        self.szul_nap = int(adat[2])
        self.kezdes_eve = int(adat[3])
        self.vegzes_eve = int(adat[4])

        self.diploma_kor = self.vegzes_eve - self.szul_ev
        self.szulinap= f'{self.szul_ho}.{self.szul_nap}'
        self.szul_ido = f'{self.szul_ev}.{self.szul_ho}.{self.szul_nap}'

    def __repr__(self):
        return f'{self.szul_ev}.{self.szul_ho}.{self.szul_nap} {self.kezdes_eve}-{self.vegzes_eve}'

hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))


# 1.Feladat
kor = int(input('Adj meg egy életkort: '))
for hallgato in hallgatok:
    if hallgato.diploma_kor < kor:
        print('Van ennél fiatalabban végzett hallgató.')
        break
else:
    print('Nincs ennél fiatalabban végzett halgató.')

fiatalok_szama = sum([1 for h in hallgatok if h.diploma_kor < kor])

# 2.Feladat 
szuletes_ho=int(input('Add meg melyik hónapban születtél (szám): '))
szuletes_nap=int(input('Add meg melyik napon születtél(szám): '))
szuletesnap= f'{szuletes_ho}.{szuletes_nap}'
for hallgato in hallgatok:
    if hallgato.szulinap == szuletesnap:
        print('Van ilyen')
        break
else:
    print('Nincs ilyen')

# 3.Feladat
legfiatalabb = hallgatok[0]
for hallgato in hallgatok:
    if hallgato.diploma_kor < legfiatalabb.diploma_kor:
        legfiatalabb = hallgato
print(f'A legfiatalabban diplomázott hallgató születési dátuma: {legfiatalabb.szul_ido}.')

# 4.Feladat
vegeztek_2016=0
for hallgato in hallgatok:
    if hallgato.vegzes_eve == 2016:
        vegeztek_2016 += 1

print(f'{vegeztek_2016} végeztek 2016-ban')
# 5.Feladat

eletkorok_2014_ben=[]
for hallgato in hallgatok:
    eletkorok_2014_ben.append(2014-hallgato.szul_ev)
print(f'{sum(eletkorok_2014_ben)//len(eletkorok_2014_ben)} volt az átlagos életkor 2014-ben.')


