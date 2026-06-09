forras=open('fakt2025\\Sipos Kristóf\\python\\11 év végi gyakorlás\\2-csapat-1.txt',mode='r',encoding='utf-8')

sor = forras.readline().strip().split(' ')
jatekos_darab = int(sor[0])
csere_darab = int(sor[1])
print(f'{jatekos_darab=}\n{csere_darab=}')

jatekosok={}
for mez_szam in range(1, jatekos_darab+1):
    jatekosok[mez_szam]= False
print(jatekosok)

for _ in range(7):
    sor = int(forras.readline().strip())
    jatekosok[sor]= True
print(jatekosok)

volt_palyan = jatekosok.copy()

for _ in range(csere_darab):
    sor=forras.readline().strip().split(' ')
    perc = int[sor[0]]
    ki = int(sor[1])
    be = int(sor[2])
    volt_palyan[be]= True
    jatekosok[be] = True
    jatekosok[ki] = False

print('voltak a pályán')
for szam, volt in volt_palyan.items():
    if volt:
        print(szam)
#print(jatekosok)
#print(volt_palyan)


