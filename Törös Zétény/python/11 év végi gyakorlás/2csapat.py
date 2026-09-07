forras = open('Törös Zétény\\python\\11 év végi gyakorlás\\2-csapat-1.txt')

sor = forras.readline().strip().split(' ')
jatekos_darab = int(sor[0])
csere_darab = int(sor[1])
print(f"{jatekos_darab=}\n{csere_darab=}")

jatekosok = {}
for mez_szam in range(1, jatekos_darab+1):
    jatekosok [mez_szam] = False
print(jatekosok)

for _ in range(7):
    sor = forras.readline().strip()
    jatekosok[sor] = True