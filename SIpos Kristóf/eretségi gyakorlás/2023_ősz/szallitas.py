adatok = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

print("2. Feladat")
össz_érték=0
for i in range(len(adatok)):
    össz_érték += adatok[i]
print(f'A tárgyak tömegének összege: {össz_érték} kg')
print("3. Feladat")
dobozok=[]
targy=adatok[0]
for i in range(len(adatok)):
    if i == 14:
        dobozok.append(targy)
        break
    elif targy + adatok[i+1] > 20:
        dobozok.append(targy)
        targy=adatok[i+1]
    else:
        targy=(targy + adatok[i+1])
össz_dobozok_szama=len(dobozok)
print(f'A dobozok tartalmának tömege (kg): {dobozok}')
print(f'A szükséges dobozok száma: {össz_dobozok_szama}')