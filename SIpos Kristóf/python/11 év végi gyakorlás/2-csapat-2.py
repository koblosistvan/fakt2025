forras=open(
    file='fakt2025\\Sipos Kristóf\\python\\11 év végi gyakorlás\\2-csapat-2.txt',
    mode='r',
    encoding='utf-8')

jatekosok ={}

kezdo=forras.readline().strip().split(',')
for i in range(len(kezdo)):
    szam= int(kezdo[i])
    jatekosok[szam] =True

volt_palyan = jatekosok.copy()
vegig_jatszott = jatekosok.copy()

for sor in forras:
    adat = sor.strip().split(';')
    perc = int(adat[0])
    ki= int(adat[1])
    be= int(adat[2])
    volt_palyan[be]= True
    jatekosok[be] = True
    jatekosok[ki] = False
