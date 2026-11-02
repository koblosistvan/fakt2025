bol = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'F', 'G', 'G', 'H']
ba =  ['B', 'D', 'F', 'C', 'D', 'E', 'G', 'E', 'H', 'G', 'H', 'I', 'J']

elek_szama = len(bol)

# Kezdetben egy várost (pl. az A jelűt) szürkére színezünk, a többit pedig fehérre. 
kezdo_varos = 'A'
szurke_sor = [kezdo_varos]
print(f'kezdo csucs: {kezdo_varos}')

fekete_latott = []
# Amíg van szürke város, addig vesszük a legrégebben szürkére festett várost: 

    # kigyűjtjük a szomszédait
    
    # Ha nincs fehér szomszédja, akkor feketére festjük. 
    # Ha van fehér szomszédja, akkor az ábécésorrendben legelsőt szürkére festjük. 
