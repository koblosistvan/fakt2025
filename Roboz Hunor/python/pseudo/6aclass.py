forras = open('fakt2025\\_Megoldások\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
adatok_szama = int(forras.readline())


class Hallgato :
    szuletesi_ev: int
    szuletesi_honap: int
    szuletesi_nap:int
    kezdes_eve: int
    befejezes_eve: int

    def __init__(self,sor):
        adat = sor.strip().split()
        self.szuletesi_ev = int(adat[0])
        self.szuletesi_honap = int(adat[1])
        self.szuletesi_nap = int(adat[2])
        self.kezdes_eve = int(adat[3])
        self.befejezes_eve = int(adat[4])


        self.diplomakor = self.befejezes_eve-self.szuletesi_ev
        self.szulinap = f'{self.szuletesi_honap:0>2d} {self.szuletesi_nap:0>2d}'
        self.szulido = f'{self.szuletesi_ev} {self.szuletesi_honap:0>2d} {self.szuletesi_nap:0>2d}'

    def __repr__(self):
        return f'{self.szuletesi_ev} {self.szuletesi_honap:0>2d} {self.szuletesi_nap:0>2d}, {self.kezdes_eve} {self.befejezes_eve}\n'



    
hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))

kor = int(input('Adj meg egy eletkort '))

for hallgato in hallgatok:
    if hallgato.diplomakor < kor:
        print('Van')
        break
else:
    print('Nincs')


szulcsinap = input('Ho nap: ')

for hallgato in hallgatok:
    if hallgato.szulinap == szulcsinap:
        print('Van')
        break
else:
    print('Nincs')

legfiatalabb = hallgatok[0]
for i in range(len(hallgatok)-1):
    if hallgatok[i].diplomakor < legfiatalabb.diplomakor:
        legfiatalabb = hallgatok[i]

print(f'A legfiatalbban vizsgazo hallgato szuletesi datuma: {legfiatalabb.szulido}')

db = 0
for hallgato in hallgatok:
    if hallgato.befejezes_eve == 2016:
        db+=1

print(db)
#676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767

a = 0
b = 0

for hallgato in hallgatok:
    if hallgato.befejezes_eve > 2014 and hallgato.kezdes_eve < 2014:
        a += 2014-hallgato.szuletesi_ev
        b+= 1

print(a/b)