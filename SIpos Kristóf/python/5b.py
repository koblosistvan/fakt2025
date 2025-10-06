forras=open('Sipos Kristóf\\python\\5b-homerseklet.txt', mode='r', encoding='utf-8')

time=[]
temp=[]

for sor in forras:
    adat= sor.strip().split('\t')
    time.append(adat[0])
    temp.append(float(adat[1]))
forras.close()

adatok_szama=len(temp)

harminc_felett=0

for i in range(1,adatok_szama):
    if temp [i] > 30:
        harminc_felett+=1

temp_up=0
temp_down=0

for i in range(1, adatok_szama):
    if temp[i] < temp[i-1]:
        temp_down+=1
    elif temp[i] > temp[i-1]:
        temp_up+=1

legmagasabb_temp=temp[0]
legmagasabb_time=0
legkisebb_time=0
legkisebb_temp= temp[0]
for i in range(1, adatok_szama):
    if legkisebb_temp > temp[i]:
        legkisebb_temp = temp[i]
        legkisebb_time= time[i]

for i in range(1, adatok_szama):
    if temp[i] > legmagasabb_temp:
        legmagasabb_temp = temp[i]
        legmagasabb_time=time[i]

print(f'A hőmérséklet {harminc_felett} szor volt 30 celziusz felett.')
print(f'Az átlag hőmérséklet {round(sum(temp)/adatok_szama,2)} celziusz volt.')
print(f'a hőmérséklet az előző méréshez képest {temp_up} szor nőt és {temp_down} szor csökkent.')
print(f'A legmagasabb mérés {legmagasabb_time} kor volt és {legmagasabb_temp} celziusz volt.')
print(f'A legalacsonyabb mérés {legkisebb_time} kor volt és {legkisebb_temp} celziusz volt.')


