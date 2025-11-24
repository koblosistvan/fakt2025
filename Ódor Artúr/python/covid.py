forras = open("Ódor Artúr\\python\\covid.txt", mode="r", encoding="utf-8")

datum = []
ujbetegek = []
halálozások = []

for sor in forras:
    adat = sor.strip().split(";")
    datum.append(adat[0])
    ujbetegek.append(int(adat[1]))
    halálozások.append(int(adat[2]))
forras.close

print(f"\n{len(datum)} nap adatit tartalmazza az állomány.")
print(f"Az összes regisztrált fertőzött száma: {sum(ujbetegek):,}\nAz összesen {sum(halálozások):,} halottat regisztráltak.")

szaz_sz = 0

for i in ujbetegek:
    if i < 100:
        szaz_sz+=1
print(f"{szaz_sz} napon volt 100 alatt az új fertőzöttek száma.")
nap_i = 0
for i in range(len(halálozások)):
    if halálozások[i] == max(halálozások):
        nap_i = i
        break
print(f"{datum[nap_i]} napon haltak meg a legtöbben.\n\t{halálozások[nap_i]}\thalott\n\t{ujbetegek[nap_i]}\tfertőzött")

legn_s = ujbetegek[1] / ujbetegek[0]
nap_i = 1
for i in range(1, len(halálozások)-1):
    if ujbetegek[i+1] / ujbetegek[i] > legn_s:
        legn_s = ujbetegek[i+1] / ujbetegek[i]
        nap_i = i+1
print(f"A legnagyobb arányú növekedés {datum[nap_i]} napon volt, amikor az előző napi adat {legn_s:.2f}-szorosa volt a fertőzöttek száma.")

n_sz = 0
cs_sz = 0
for i in range(len(halálozások) - 1):
    if halálozások[i] > halálozások[i+1]:
        cs_sz += 1
    elif halálozások[i] < halálozások[i+1]:
        n_sz += 1
        
print(f"{n_sz} napon nőtt a halálozások száma az előzőhöz képest.")
print(f"{cs_sz} napon csökent a halálozások száma az előzőhöz képest.")
print(f"{sum(halálozások) / len(halálozások):.1f} ember halt meg átlagosan naponta.")