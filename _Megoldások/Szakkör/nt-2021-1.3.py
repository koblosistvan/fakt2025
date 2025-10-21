bol = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'F', 'G', 'G', 'H']
ba =  ['B', 'D', 'F', 'C', 'D', 'E', 'G', 'E', 'H', 'G', 'H', 'I', 'J']
elek_szama = len(bol)

kezdo_varos = 'A'
# Kezdetben egy várost (pl. az A jelűt) szürkére színezünk, a többit pedig fehérre. 
szurke_sor = [kezdo_varos]
print(kezdo_varos)
fekete_latott = []

# Amíg van szürke város, addig vesszük a legrégebben szürkére festett várost: 
while len(szurke_sor) > 0:
    varos = szurke_sor[0]

    # kigyűjtjük a szomszédait
    szomszedok = []
    for i in range(elek_szama):
        if bol[i] == varos:
            szomszedok.append(ba[i])
        if ba[i] == varos:
            szomszedok.append(bol[i])
    szomszedok.sort()
    
    # Ha nincs fehér szomszédja, akkor feketére festjük. 
    # Ha van fehér szomszédja, akkor az ábécésorrendben legelsőt szürkére festjük. 
    for szomszed in szomszedok:
        if szomszed not in szurke_sor and szomszed not in fekete_latott:
            szurke_sor.append(szomszed)
            print(szomszed)
    fekete_latott.append(varos)
    szurke_sor = szurke_sor[1:]
    
