forras=open('Sipos Kristóf\\pythom\\6b-forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

hely=[]
ora=[]
perc=[]
ido=[]

for sor in forras:
    adat=sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close()

meresek_szama=len(hely)

legnagyobb= ido[1]-ido[0]
legnagyobb_index=0

for i in range(1,meresek_szama):
    if ido[i+1]-ido[i] > legnagyobb:
        legnagyobb = ido[i+1] - ido[i]
        legnagyobb_index = i

print('')
