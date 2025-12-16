while True:
    meg_szam=input("Adj meg egy számot: ")
    if meg_szam == '0':
        break
    szamj_osszeg = 0
    for i in meg_szam:
        szamj_osszeg += int(j)
    print(f'A számjegyek összege: {szamj_osszeg}')