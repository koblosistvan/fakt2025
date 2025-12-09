forras=open('Sipos Kristóf\\python\\fenyőfa\\fenyofa.txt',mode='r',encoding='utf-8')

adat= forras.readline().strip().split(' ')
sorok_szama,oszlopok_szama=int(adat[0]),int(adat[1])

pixele=[]
for i in range(sorok_szama):
    for j in range(oszlopok_szama):
        pixel=forras.readline().strip()
        
forras.close
