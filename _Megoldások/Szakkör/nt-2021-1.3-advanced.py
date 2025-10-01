graf = {
    'A': ['B', 'D', 'F'],
    'B': ['A', 'C', 'D', 'E', 'G'],
    'C': ['B', 'E', 'H'],
    'D': ['A', 'B'],
    'E': ['B', 'C'],
    'F': ['A', 'G'],
    'G': ['B', 'I', 'H'],
    'H': ['C', 'G', 'J'],
    'I': ['G'],
    'J': ['H']
}

sor, latott = [], []

kezdo_varos = 'A'

# Kezdetben egy várost (pl. az A jelűt) szürkére színezünk, a többit pedig fehérre. 
sor.append(kezdo_varos)
print(kezdo_varos)

# Amíg van szürke város, addig vesszük a legrégebben szürkére festett várost: 
while len(sor) > 0:
    csucs = sor[0]
    
    # Ha nincs fehér szomszédja, akkor feketére festjük. 
    # Ha van fehér szomszédja, akkor az ábécésorrendben legelsőt szürkére festjük. 
    for szomszed in sorted(graf[csucs]):
        if szomszed not in sor and szomszed not in latott:
            sor.append(szomszed)
            print(szomszed)
    latott.append(csucs)
    sor = sor[1:]
    
