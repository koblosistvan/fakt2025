forras= open('Szmodis Vince\\python\\11 év végi gyakorlás\\1-gyongy-1.txt', mode='r', encoding='utf-8')
adat=forras.readline().strip()

forras.close()
print(adat)

forras= open('Szmodis Vince\\python\\11 év végi gyakorlás\\1-gyongy-2.txt', mode='r', encoding='utf-8')
adat=forras.readline().strip()
adat=adat.split()
forras.close()

print(adat)

forras= open('Szmodis Vince\\python\\11 év végi gyakorlás\\1-gyongy-3.txt', mode='r', encoding='utf-8')
adat = []
for sor in forras:
    adat.append(sor.strip())
forras.close()
print(adat)

forras= open('Szmodis Vince\\python\\11 év végi gyakorlás\\1-gyongy-4.txt', mode='r', encoding='utf-8')
forras.readline()
adat = []

for sor in forras:
    adat.append(sor.strip())
forras.close()

print(adat)

szinek = []
for g in adat:
    if g not in szinek:
        szinek.append(g)

print(f"A nyajláncon {len(szinek)} féle gyöngy van ")


for i in range(len(adat)):
    if adat[i-1]==adat[i]:
        print('Van egymás mellett két ugyanolyan gyöngy')
        break

else:
    print('Nincs  egymás mellett két ugyanolyan gyöngy')    



m = int(input('Milyen hosszúságút keresel: '))
n = 1
for i in range(-len(adat)+1,len(adat)):
    if adat[i-1]==adat[i]:
        n+=1
        if n==m:
            print('Van ilyen hosszú')
            break
    else: 
        n=1
else:
    print('Nincs ennyi ugyanolyan gyöngy egymás melett')