# 1. feladat: Milyen programozási tételeket (alap algoritmusokat) ismersz? Sorold fel őket!
# ide írd


# 2. feladat: egészítsd ki!
# A program egy hőmérséklet adatokat tartalmazó listát kapt (h)
# A feladata, hogy megszámolja, hány volt "csúcs", azaz magasabb a hőmérséklet, mint a szomszédős napokon
h = [4, 6, 3, 5, 7, 8, 9, 11, 8, 9, 10, 6, 5, 4, 6]
# ide írd a programot
n = 0
for i in range(1, len(h)-1):
    if h[i] > h[i-1] and h[i] > h[i+1]:
        n += 1
print(f'Összesen {n} napon volt "csúcs".')


# 3. feladat: mit ír ki a program?
a = [2, 3, 5, 7, 11, 13, 17]
print(a[3])
# ide írd
print(a[:3])
# ide írd
print(a[3:5])
# ide írd
print(a[5:])
b = 1
for i in range(2, 6, 2):
    b *= a[i]

print(b)
# ide írd


print([p for p in a if p < 5])
# ide írd


