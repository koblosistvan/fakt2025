hova = input('Hava szeretnél utazni: ')
print(f"Természetesen van utunk {hova} felé.")
menyi = int(input("Mennyi pénzed van az útra: "))
ár = menyi/3*2
print(f"Az utazás ára {ár:.1f} Ft.")
print("Az idegen forgalmi illeték összege: 5,000 Ft.")
print(f"Az utazás teljes ára: {ár+5000:.1f}",)
valasz = input("Elfogadod az ajánlatot? (I/N) ")

if valasz == "I" :
    hany = int(input("Hányan utaznátok: "))
    x = 1
    for x in range(hany):
        input(f"Add meg a {x+1}. utas nevét: ")
        x += 1
    print(f"Rögzítettem a megrendelést {hany} főre a {hova} úticéllal. Viszont chatelésre.")
else:
    print("Akkor menj a faszomba")