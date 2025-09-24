szoveg = str(input("Adj meg egy szöveget: "))

szamlalo = 0
gy_szamlalo = 0
maganhangzok = ["a", "á", "e", "é", "i", "í", "u", "ú", "ü", "ű", "o", "ó", "ö", "ő"]
for i in range(len(szoveg)):
    betu = szoveg[i]
    if betu in maganhangzok:
        szamlalo += 1 
for i in range(len(szoveg)-1):
    if szoveg[i] == "g" and szoveg[i + 1] == "y":
        gy_szamlalo += 1
print(f"{szamlalo}\n{gy_szamlalo}")