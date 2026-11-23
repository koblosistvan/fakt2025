def pozitiv_szamok_osszegzese(t):
    osszes = 0
    for i in range(len(t)):
        if t[i] > 0:
            osszes += t[i]
    print(osszes)
pozitiv_szamok_osszegzese([4,-3,2,-1])