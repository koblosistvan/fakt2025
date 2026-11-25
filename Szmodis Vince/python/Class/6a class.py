forras = open('_Megoldások\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
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
        self.szulinap = f'{self.szul_ho}.{self.szul_nap}'
        self.szul_ido = f'{self.szul_ev}.{self.szul_ho}.{self.szul_nap}'

    def __repr__(self):
        return f'{self.szul_ev}.{self.szul_ho}.{self.szul_nap} {self.kezdes_eve}-{self.vegzes_eve}'


hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))

#1. feladat
kor = int(input('Adj meg egy életkort: '))
for hallgato in hallgatok:
    if hallgato.diploma_kor < kor:
        print('Van ennél fiatalabban végzett hallgató')
        break
else:
    print('Nincs ennél fiatalabban végzett hallgató')

fiatalok_szama = sum([1 for h in hallgatok if h.diploma_kor < kor])
print(fiatalok_szama)

#2. feladat
for halgato in hallgatok:
    if hallgato.szul_ho == 12 and hallgato.szul_nap == 4:
        print('Van aki veled egy napon született')
else:
    print('Nem született veled senki egy napon')

#3. feladat
legfiatalabb = hallgatok[0]
for i in range(len(hallgatok)):
    if hallgatok[i].diploma_kor < legfiatalabb.diploma_kor:
        legfiatalabb = hallgatok[i]
print(f'A legfiatalabban dipomázott hallgató születési dátuma: {legfiatalabb.szul_ido}.')

#4. feladat
tizenhatban_vegzett = 0
for i in range(len(hallgatok)):
    if hallgatok[i].vegzes_eve == 2016:
        tizenhatban_vegzett+=1
print(f'{tizenhatban_vegzett} tanuló végzett 2016-ban')

#5. feladat
atlageletkor = 0
for i in range(len(hallgatok)):
    atlageletkor+=hallgatok[i].vegzes_eve-hallgatok[i].szul_ev
atlageletkor/len(hallgatok)

print(atlageletkor)