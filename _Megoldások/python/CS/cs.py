from dataclasses import dataclass
@dataclass
class Meccs:
    idopont: str
    palya: str
    csapat: str
    pont: int
    pont_kulonbseg: int
    eredmeny: str

def f(n):
    print('\n' + '-'*40)
    print(f'{n}. feladat')


meccsek = []
forras = open('_Megoldások\\python\\CS\\cs.csv', mode='r', encoding='utf-8')
forras.readline()

for sor in forras:
    adat = sor.strip().split(';')
    meccs = Meccs(
        idopont=adat[0], 
        palya=adat[1],
        csapat=adat[2],
        pont=int(adat[3]),
        pont_kulonbseg=int(adat[4]),
        eredmeny=adat[5]
    )
    meccsek.append(meccs)

forras.close()

f(1)
print(f'Az adatfájl {len(meccsek)//2:,} meccs adatait tartalmazza.')

f(2)
print(f'Az első meccs időpontja: {min(meccsek, key=lambda x: x.idopont).idopont}.')

f(3)
meccsek.sort(key=lambda x: x.pont_kulonbseg)
print('Az adatokat rendeztem pontkülönbség szerint.)')

f(4)
print(f'{len(set([m.palya for m in meccsek]))} pályán folytak meccsek.')

f(5)
extra_salt = [m for m in meccsek if m.csapat == 'Extra Salt']
print('Extra Salt statisztika:')
print(f'\t- a csapat {len(extra_salt)} meccset játszott')
extra_salt_eredmeny = [m.eredmeny for m in extra_salt]
print(f'\t- eredményei: {extra_salt_eredmeny.count('győzelem')} győzelem / {extra_salt_eredmeny.count('vereség')} vereség / {extra_salt_eredmeny.count('döntetlen')} döntetlen') 
extra_salt_pontkulonbseg = [m.pont_kulonbseg for m in extra_salt]
print(f'\t- a legnagyobb pontkülönbség {max(extra_salt_pontkulonbseg)}, a legkisebb pontkülönbség {min(extra_salt_pontkulonbseg)} volt')
print(f'\t- az átlagos pontkülönbség {sum(extra_salt_pontkulonbseg) / len(extra_salt_pontkulonbseg):.2f} volt')
