forras = open("Ódor Artúr\\python\\5b-homerseklet.txt", mode= "r", encoding="utf-8")

ido = []
homersekletek = []
harmincfelett = 0
atlaghom = 0

for sor in forras:
    adat = sor.strip().split("\t")
    ido.append(adat[0])
    homersekletek.append(float(adat[1]))
forras.close()

for hom in homersekletek:
    if hom > 30:
        harmincfelett += 1
    atlaghom += hom
 
nagyobb_mint_elozo = 0
kissebb_mint_elozo = 0
legnagyobb_emelkedes = homersekletek[1] - homersekletek [0]
ido_index1, ido_index2 = ido[0], ido[1]



for i in range(len(homersekletek)- 1):
    if homersekletek[i] > homersekletek[i + 1]:
        nagyobb_mint_elozo += 1
    elif homersekletek[i] < homersekletek[i + 1]:
        kissebb_mint_elozo += 1
    if homersekletek[i + 1] - homersekletek[i] > legnagyobb_emelkedes:
        legnagyobb_emelkedes = homersekletek[i + 1] - homersekletek[i]
        ido_index1, ido_index2 =ido[homersekletek.index(homersekletek[i])], ido[homersekletek.index(homersekletek[i + 1])]

kulonbseg = (homersekletek[0] - homersekletek[1]) + (homersekletek[2] - homersekletek[1])
leggyanusabb = homersekletek[1]
leggyanusabb_index = 1

for i in range(1, len(homersekletek) - 1):
    if (homersekletek[i - 1] - homersekletek[i]) + (homersekletek[i + 1] - homersekletek[i]) > kulonbseg:
        leggyanusabb = homersekletek[i]
        kulonbseg = (homersekletek[i - 1] - homersekletek[i]) + (homersekletek[i + 1] - homersekletek[i])
        leggyanusabb_index = i 

    
    
print(f"{harmincfelett}-szer volt 30 felett.\n{atlaghom / len(homersekletek):.2f} volt az átlag hőmérséklet"
      f"\n{nagyobb_mint_elozo} volt nagyobb hőmérséklet, mint az előző."
      f"\n{kissebb_mint_elozo} volt kissebb hőmérséklet, mint az előző."
      f"\n{ido[homersekletek.index(min(homersekletek))]}-kor volt a legalacsonyabb hőmérséklet és {min(homersekletek)}°C volt"
      f"\n{ido[homersekletek.index(max(homersekletek))]}-kor volt a legalacsonyabb hőmérséklet és {max(homersekletek)}°C volt"
      f"\n{legnagyobb_emelkedes:.2f} volt a legnagyobb emelkedés {ido_index1} és {ido_index2} között."
      f"\nA leggyanúsabb érés {leggyanusabb}°C volt, {ido[leggyanusabb_index]}-kor")