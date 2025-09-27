import random

jeles = 96
dolgozatok_szama = 100
dolgozatok = []
for i in range(dolgozatok_szama):
    pontszam = random.randint(0, 120)
    dolgozatok.append(pontszam)

szamlalok = [] 
for i in range(20):
    szamlalok.append(0)
    
for i in range(len(dolgozatok)):
    if dolgozatok[i] >= jeles:
       szamlalok[-1] += 1 
    elif dolgozatok[i] < 96 and dolgozatok[i] >= jeles-3:
        szamlalok[-2] += 1
    if dolgozatok[i] == 120:
        szamlalok[-3] += 1
        
    szamlalok[-4] += dolgozatok[i]
        
        
        
    szamlalok[int(((dolgozatok[i] / 120 * 100) // 10))] += 1
    
szamlalok[9] += szamlalok[10]
szamlalok[-4] /= dolgozatok_szama

print(f"Jeles dolgozatok: {szamlalok[-1]}\nJeles közeli dolgozatok: {szamlalok[-2]}\nMax " 
      f"pontos dolgozat: {szamlalok[-3]}\nÖsszes dolgozat átlaga: {szamlalok[-4]}")

for i in range(10):
    print(f"Akár {(i + 1) * 10}%-ot elérő dolgozatok: {szamlalok[i]}")