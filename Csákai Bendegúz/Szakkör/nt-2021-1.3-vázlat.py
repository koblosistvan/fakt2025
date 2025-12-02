bol = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'F', 'G', 'G', 'H']
ba =  ['B', 'D', 'F', 'C', 'D', 'E', 'G', 'E', 'H', 'G', 'H', 'I', 'J']
elek_szama = len(bol)

# Kezdetben egy várost (pl. az A jelűt) szürkére színezünk, a többit pedig fehérre. 
kezdo = str(input('Add meg a kezdő várost: '))
szurke_sor = [kezdo]
print(f'Kezdő csúcs: {kezdo}')
fek_lat = []

while len(szurke_sor) > 0:
    varos = szurke_sor[0]
    szomszed = []
    for i in range(elek_szama):
        if bol[i] == varos:
            szomszed.append(ba[i])
        if ba[i] == varos:
            szomszed.append(bol[i])
    szomszed.sort()
    for i in range(len(szomszed)):
        if szomszed[i] not in szurke_sor and szomszed[i] not in fek_lat:
            szurke_sor.append(szomszed[i])
            print(szomszed[i])
    fek_lat.append(varos)
    szurke_sor = szurke_sor[1:]
