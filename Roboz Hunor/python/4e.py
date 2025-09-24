szoveg = 'S egy égi kar intene, hogy énekelhető egy dal, amit a Babits Mihály bácsi írt nekünk: Mire Micimackó megjegyezné, hogy énekelni jó. És Bagoly persze mondaná, hogy a pszichózis bonyolult, És Nyuszinak eszébe jutna, hogy épp valamit nagyon keres, De Micimackó azt mondaná, tudod, ez olyan, mint a méz.'
maganhangzo = ["a","á","e","é","u","o","ö","ü","ó","ő","ú","ű"]

maganhangzok_szama = 0

for i in range(len(szoveg)):
    if szoveg[i] in maganhangzo:
        maganhangzok_szama +=1
print(maganhangzok_szama)