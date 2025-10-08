bol = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'F', 'G', 'G', 'H']
ba =  ['B', 'D', 'F', 'C', 'D', 'E', 'G', 'E', 'H', 'G', 'H', 'I', 'J']
elek_szama= len(bol)
# Kezdetben egy várost (pl. az A jelűt) szürkére színezünk, a többit pedig fehérre. 
kezdo_varos= 'A'
szurke_sor = [kezdo_varos]
print(f'Kezdő csúcs: {kezdo_varos}.')
fekete_latott= []
# Amíg van szürke város, addig vesszük a legrégebben szürkére festett várost: 
while len(szurke_sor) > 0:
    varos =szurke_sor[0]
    # kigyűjtjük a szomszédait
    szomszedok=[]
    for i in range(elek_szama):
        if bol[i] == varos:
            szomszedok.append(ba[i])
        if ba[i] == varos:
            szomszedok.append(bol[i])
             
    # Ha van fehér szomszédja, akkor az ábécésorrendben legelsőt szürkére festjük. 
    szomszedok.sort()
    for i in range(len(szomszedok)):
        if szomszedok[i] not in szurke_sor and szomszedok[i] not in fekete_latott:
            szurke_sor.append(szomszedok[i])
            print(szomszedok[i])
    # Ha nincs fehér szomszédja, akkor feketére festjük.
    fekete_latott.append (varos)
    szurke_sor = szurke_sor[1:]