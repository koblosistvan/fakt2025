forras = open('Dobai Balint\\futar\\futar.txt', mode ='r', encoding='utf-8')
forras.readline()

nap ,  fuvar_szama ,  tavolsag = [] , [] , []


for sor in forras:
    adat = sor.strip().split(' ')
    nap.append(int(adat[0]))
    fuvar_szama.append(int(adat[1]))
    tavolsag.append(int(adat[2]))
forras.close()
def f(n):
    print(f'\n {n}. feladat')

f(1)
leghosszabb_tav = tavolsag[0]
leghosszabb_sorszam = fuvar_szama[0]
leghosszabb_nap = nap[0]
for i in range(len(nap)):
    if tavolsag[i] > leghosszabb_tav:
        leghosszabb_tav = tavolsag[i]
        leghosszabb_nap = nap[i]
        leghosszabb_sorszam = fuvar_szama[i]
print(f'A leghosszabb fuvar a {leghosszabb_nap}. napon volt a {leghosszabb_sorszam} fuvar, amely {leghosszabb_tav} volt')

f(2)
szerda_tav = 0
for i in range(len(nap)):
    if nap[i] == 3:
        szerda_tav +=tavolsag[i]
print(f'A harmadik napon osszesen {szerda_tav} km-t tett meg')
 
f(3)
negyediken_fuvar = 0
for i in range(len(nap)):
    if nap[i] == 4:
        negyediken_fuvar +=1

print(f'A negyedik napon {negyediken_fuvar} fuvart teljesitett')

f(4)
for i in range(len(nap)):
    if tavolsag[i] > 20:
        print('Volt 20km-nel hosszabb fuvar')
        break
    else:
        print('Nem volt 20km-nel hosszabb fuvar')
        break

