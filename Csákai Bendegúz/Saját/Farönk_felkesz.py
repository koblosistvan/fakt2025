import math

sz = 18#int(input('Szélesség: '))
m = 14#int(input('Magaasság: '))
r = 1#int(input('Körök sugara: '))
para = math.floor((sz/(2*r)))
paro = math.floor(((sz-r)/(2*r))) 
sorok = math.floor((((m-(2*r))/(r*(3**0.5)))+1)) 
para_sorszam = 0
paro_sorszam = 0
if (sorok/2) % 2 == 0:
    para_sorszam = sorok/2
    paro_sorszam = sorok/2
else:
    if (sorok/2) % 2 != 0 and paro_sorszam %2 != 0:
        para_sorszam = math.ceil((sorok/2))
        paro_sorszam = math.floor((sorok/2)-0.5)
    elif (sorok/2) % 2 != 0 and paro_sorszam %2 != 0 and para_sorszam % 2 != 0:
        para_sorszam = math.ceil((sorok/2)+0.5)
        paro_sorszam = math.floor((sorok/2)-0.5)
faronk = (para_sorszam*para) + (paro_sorszam*paro) 
print(f'A sorok száma: {sorok}')
print(f'A páratlan sorokban lévő farönkök száma: {para}')
print(f'A páros sorokban lévő farönkök száma: {paro}')
print(f'A páros és páratlan sorok aránya: {para_sorszam:.0f}:{paro_sorszam:.0f}')
print(f'Összesen {faronk:.0f} rönk lehet bent.')