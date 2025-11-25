forras = open('Dobai Balint\\python\\cs.csv', mode ='r', encoding='utf-8')
forras.readline()
idopont = []
palya = []
csapat = []
pont = []
pont_kul = []
eredmeny = []

for sor in forras:
    adat = sor.strip().split(';')
    idopont.append(str(adat[0]))
    palya.append(str(adat[1]))
    csapat.append(str(adat[2]))
    pont.append(int(adat[3]))
    pont_kul.append(int(adat[4]))
    eredmeny.append(str(adat[5]))
forras.close()
adat = len(csapat)
print(f'az allomanyban {adat/2:.0f} meccs adatai vannak')