forras = open('Törös Zétény\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
forras.readline()
class Hallgato:
    szul_ev = []
    szul_honap = []
    szul_nap = []
    kezdes_ev = []
    vegzes_ev = []

    def __init__(self, sor):
        adat = sor.strip().split()
        self.szul_ev = int(adat[0])
        self.szul_honap = int(adat[1])
        self.szul_nap = int(adat[2])
        self.kezdes_ev = int(adat[3])
        self.vegzes_ev = int (adat[4])
        self.diploma_kor = self.vegzes_ev - self.szul_ev


hallgatok = []
for sor in forras:
    hallgatok.append(Hallgato(sor))

szulinap = "01.08"
for hallgato in hallgatok:
    if hallgato.szul_nap == szulinap:
        print()
        break
else:
    print()

legfiatalabb = hallgatok[0]
for hallgato in hallgatok:
    if hallgato.diploma_kor < legfiatalabb.diploma_kor:
        legfiatalabb = hallgato

x = 0
for hallgato in hallgatok:
    if hallgato.vegzes_ev == 2016:
        x += 1

print(x)

for hallgato in hallgatok:
    if hallgato.szul_ev 