import time
forras = open('fakt2025\\_Feladatok\\python\\CS\\cs.csv', mode='r',encoding='utf-8')
forras.readline()
idő,pálya,csapat,pont,különbség,eredmény = [],[],[],[],[],[]

for sor in forras:
        adat = sor.strip().split(';')
        idő.append(adat[0])
        pálya.append(adat[1])
        csapat.append(adat[2])
        pont.append(int(adat[3]))
        különbség.append(int(adat[4]))
        eredmény.append(adat[5])
forras.close()

print(f'{int(len(csapat)/2)} meccs adatai vannak az állományban')
print(f'Az első meccs {min(idő)}-kor volt')


"""for i in range(len(különbség)):
    for k in range(len(különbség)-i-1):
        if különbség[k] < különbség[k+1]:
            idő[k],idő[k+1] = idő[k+1],idő[k]
            pálya[k],pálya[k+1] = pálya[k+1],pálya[k]
            csapat[k],csapat[k+1] = csapat[k+1],csapat[k]
            pont[k],pont[k+1] = pont[k+1],pont[k]
            különbség[k],különbség[k+1] = különbség[k+1],különbség[k]
            eredmény[k],eredmény[k+1] = eredmény[k+1],eredmény[k]"""

start = time.time()

i = 0
n = len(idő)
while i < n-1:
    if különbség[i] <= különbség[i+1]:
        i+=1
    else:
        idő[i],idő[i+1] = idő[i+1],idő[i]
        pálya[i],pálya[i+1] = pálya[i+1],pálya[i]
        csapat[i],csapat[i+1] = csapat[i+1],csapat[i]
        pont[i],pont[i+1] = pont[i+1],pont[i]
        különbség[i],különbség[i+1] = különbség[i+1],különbség[i]
        eredmény[i],eredmény[i+1] = eredmény[i+1],eredmény[i]
        if i > 0:
            i-=1

end = time.time()
print(f'Összesen {len(set(pálya))} pálya van')

extra_salt_meccs = 0
for i in range(len(csapat)):
    if csapat[i] == 'Extra Salt':
        extra_salt_meccs +=1
print(f'Összesen {extra_salt_meccs} meccset játszott az Extra Salt csapat')

nyert, vesztett, döntetlen = 0,0,0

for i in range(len(csapat)):
    if csapat[i] == 'Extra Salt':
        if eredmény[i] == 'vereség':
              vesztett+=1
        elif eredmény[i] == 'győzelem':
            nyert+=1
        else: döntetlen+=1
print(f'Az Extra Salt csapat {nyert}x győzőtt {döntetlen}x játszott döntetlent és {vesztett}x vesztett')

e_kül = []
for i in range(len(csapat)):
    if csapat[i] == 'Extra Salt':
        e_kül.append(különbség[i])
print(f'A legkisebb pontkülönbség: {min(e_kül)}, a legnagyobb: {max(e_kül)}')
print(f'{sum(e_kül)/len(e_kül):.2f} volt az átlagpontszám')

print(end-start)