forras = open("Ódor Artúr\\python\\5a-magasugras2.txt", mode= "r", encoding="utf-8")
tavaly= []
iden =[]

for sor in forras:
    adat = sor.strip().split(";")
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))
forras.close

legalacsonyabb_index = tavaly[0]
legalacsonyabb = legalacsonyabb_index
legmagasabb_index = tavaly[0]
legmagasabb = legmagasabb_index
legnagyobbfejlodes_i = 0
legnagyobb_fejlodes = iden[0] - tavaly[0]
visszaeses_i = 0
visszaeses = tavaly[0] - iden[0]


for i in range(1, len(tavaly)):
    if tavaly[i] > legmagasabb:
        legmagasabb = tavaly[i]
        legmagasabb_index = i
    if tavaly[i] < legalacsonyabb:
        legalacsonyabb = tavaly[i]
        legalacsonyabb_index = i
    if iden[i] - tavaly[i] > legnagyobb_fejlodes:
        legnagyobbfejlodes_i = i
        legnagyobb_fejlodes = iden[i] - tavaly[i]   
    if tavaly[i] -iden[i] > visszaeses: 
       visszaeses = tavaly[i] -iden[i]
       visszaeses_i = i



print(f"\nA legmagasabb ugrás tavaly {legmagasabb}cm volt, ami a {legmagasabb_index + 1}. ugrás volt."
      f"\nA legalacsonyabb ugrás tavaly {legalacsonyabb}cm volt, ami a {legalacsonyabb_index + 1}. ugrás volt."
      f"\nA legnagyobb fejlődést a {legnagyobbfejlodes_i + 1}. ember érte el, {tavaly[legnagyobbfejlodes_i]} => {iden[legnagyobbfejlodes_i]}"
      f"\nA legnagyobb visszaesést a {visszaeses_i + 1}. ember érte el, {tavaly[visszaeses_i]} => {iden[visszaeses_i]}.")