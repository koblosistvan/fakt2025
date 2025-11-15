ut = input("Hova szeretnél utazni? ")
print(f"Nyugi, van út {ut} felé.")
penzed = int(input("Mennyi pénzed van? "))
print(f"Az utazás ára: {2/3 * penzed:.2f}ft.")
illetek = 5000
print(f"Az idegen forgalmi illeték összege: {illetek} ft.")
print(f"Az út teljes költsége: {illetek + 2/3*penzed} ft.")
ajanlat=input("Elfogadod az ajánlatot? (I/N): ")
if ajanlat == "N":
    print("Viszlát legközelebb")
elif ajanlat == "I":
    utasok = int(input("Hányan utaznátok? "))
    for i in range(utasok):
        utas = input(f"Add meg az {i+1}. utas nevét: ")
    print(f"Rögzítettem az utat {ut}-be. {utasok} fő részére. Viszont látásra!")