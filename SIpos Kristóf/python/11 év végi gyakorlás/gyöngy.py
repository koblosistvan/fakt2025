#1.fájl
forrás=open("Sipos Kristóf\\python\\11 év végi gyakorlás\\1-gyongy-1.txt",mode='r',encoding='utf-8')
adat =forrás.readline().strip()
adat = list(adat)
forrás.close()

print(adat)

#2.fájl
forrás=open('Sipos Kristóf\\python\\11 év végi gyakorlás\\1-gyongy-2.txt', mode='r', encoding='utf-8')
adat =forrás.readline().strip()
adat = adat.split()
forrás.close()
print(adat)

#3.fájl
forrás=open('Sipos Kristóf\\python\\11 év végi gyakorlás\\1-gyongy-3.txt',mode='r',encoding='utf-8')
adat=[]
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

#4.fájl
forrás=open('Sipos Kristóf\\python\\11 év végi gyakorlás\\1-gyongy-4.txt',mode='r',encoding='utf-8')
adat=[]
forrás.readline()
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

#Feladat 1
color=[]
for g in adat:
    if g not in color:
        color.append(g)
print(f'A nyakláncon {len(color)} színű gyöngy van')

#Feladat 2
egymas_mellett= False
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        egymas_mellett=True
        print('Vannak egymás melletti adatok.')
        break
else:
    print('Nicsenek egymás melletti adatok.')

#Feladat plusz 1
m = int(input('Menyi gyöngyöt szertnél hogy egymás után legyen egy sorban: '))
n = 0
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        n += 1
        if n == m:
            print('Van ilyen hosszú egymás után következő gyöngy.')
            break
    else:
        n = 1
else:
    print('Nincs ennyi egymás után következő gyöngy.')


        
   
