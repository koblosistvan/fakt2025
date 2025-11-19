forras = open('fakt2025\\_Feladatok\\python\\IMDB\\imdb.txt', mode='r',encoding='utf-8')
forras.readline()
év,idő,értékelés,rendező,bevétel,cím = [],[],[],[],[],[]
for sor in forras:
    adat = sor.strip().split('\t')
    év.append(adat[0])
    idő.append(adat[1])
    értékelés.append(adat[2])
    rendező.append(adat[3])
    bevétel.append(adat[4])
    cím.append(adat[5])
forras.close()
sor=len(cím)

print(f'{sor} film adatai vannak az állományban')

