forras = open("Ódor Artúr\\python\\6a-hallgatok.txt", mode= "r", encoding="utf-8")
adatok_sz = int(forras.readline())

szuletesi_ev = []
szuletesi_ho = []
szuletesi_nap = []
kezdes_eve = []
befejezes_eve = []

for sor in forras:
    adat = sor.strip().split(" ")
    szuletesi_ev.append(int(adat[0]))
    szuletesi_ho.append(int(adat[1]))
    szuletesi_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    befejezes_eve.append(int(adat[4]))
forras.close

eletkor = int(input("Add meg a korod: "))
for i in range(adatok_sz):
    kor = befejezes_eve[i] -szuletesi_ev[i]
    if kor < eletkor:
        print(f"Van {eletkor} évnél fiatalabb végzett.")
        break
else:
    print(f"Nincs {eletkor} évnél fiatalabb.")

ho, nap = map(int, input("Add meg melyik hónapban van a születés napod (pl.:02.30): ").strip().split("."))

for i in range(len(kezdes_eve)):
    if int(ho) == szuletesi_ho[i] and int(nap) == szuletesi_nap[i]:
        print("Van akinek ugyan azon a nap van a születésnapja.")
        break
else:
    print("Nincs olyan akinek ezen a nap van a születés napja.")

legfiatalabb_vegzett = befejezes_eve[1] - szuletesi_ev[1]
legfi_szul = szuletesi_ev[0]
legfi_ho = szuletesi_ho[0]
legfi_nap = szuletesi_nap[0]

for i in range(len(kezdes_eve)):
    if befejezes_eve[i] - szuletesi_ev[i] < legfiatalabb_vegzett:
        legfiatalabb_vegzett = befejezes_eve[i] - szuletesi_ev[i]
        legfi_szul, legfi_ho, legfi_nap = szuletesi_ev[i], szuletesi_ho[i], szuletesi_nap[i]
    elif befejezes_eve[i] - szuletesi_ev[i] == legfiatalabb_vegzett and szuletesi_ho[i] > legfi_ho:
        legfiatalabb_vegzett = befejezes_eve[i] - szuletesi_ev[i]
        legfi_szul, legfi_ho, legfi_nap = szuletesi_ev[i], szuletesi_ho[i], szuletesi_nap[i]
    elif befejezes_eve[i] - szuletesi_ev[i] == legfiatalabb_vegzett and szuletesi_ho[i] == legfi_ho and szuletesi_nap[i] > legfi_nap:
        legfiatalabb_vegzett = befejezes_eve[i] - szuletesi_ev[i]
        legfi_szul, legfi_ho, legfi_nap = szuletesi_ev[i], szuletesi_ho[i], szuletesi_nap[i]

print(f"A legfiatalabb végzett szülcsinapcsija {legfi_szul}. {legfi_ho}. {legfi_nap}. ")      

vegzett_2016ban = 0

for data in befejezes_eve:
    if data == 2016:
        vegzett_2016ban += 1
    
print(f"{vegzett_2016ban} halgató")

tavsz_osszeg = 0
tanulok_sz = 0

for i in range(len(befejezes_eve)):
    if kezdes_eve[i] <= 2014 and befejezes_eve[i] >= 2014:
        tavsz_osszeg += 2014 - szuletesi_ev[i]
        tanulok_sz += 1

print(f"{tavsz_osszeg / tanulok_sz} volt az átlag életkor. ")