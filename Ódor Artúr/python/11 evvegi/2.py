print()
adat = None
forras = r"Ódor Artúr\python\11 evvegi\11 év végi gyakorlás\2-csapat-1.txt"
with open(forras, "r") as f:
    #f.readline
    #adat = f.read().replace("\n", "").replace(",","").replace(" ","")
    sor = f.readline().strip().split(" ")
    jatekos_db, csere_db = int(sor[0]), int(sor[1])
    jatekos = {}
    
    for mez_szam in range(1, jatekos_db+1):
        jatekos[mez_szam] = False

    for _ in range(7):
        a = int(f.readline().strip())
        jatekos[a] = True

    volt_palyan = jatekos.copy()
    cser_jatekos = jatekos.copy()
    ido_jatekosok = jatekos.copy()

    for i in range(len(jatekos)):
        ido_jatekosok[i] = 0
    


    for _ in range(csere_db):
        sor = f.readline().strip().split(" ")
        perc = int(sor[0])
        ki = int(sor[1])
        be = int(sor[2])
        ido_jatekosok[ki] += perc
        ido_jatekosok[be] -= perc
        cser_jatekos[ki] = False
        volt_palyan[be] = True
        jatekos[be] = True
        jatekos[ki] = False
    

print("Végig játszó játékosok: ", end="")
for nev, csere in cser_jatekos.items():
    if csere == True:
        print(f"{nev}", end=" ")
print("\nEzek a játékosok voltak a pályán: ", end="")
for jat, volt in volt_palyan.items():
    if volt == True:
        print(f"{jat}", end=" ")