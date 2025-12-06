kerdesek_szama = int(input())
kezd,veg = [],[]
for i in range(kerdesek_szama):
    kerd = input().split()
    kezd.append(int(kerd[0]))
    veg.append(int(kerd[1]))
ö = []
for i in range(len(kezd)):
    for j in range(kezd[i], veg[i]+1):
        ö.append(j)

összeg = []     

for i in range(len(ö)):
    szam = ö[i]
    while szam >= 10:  
        ossz = 0
        szam_str = str(szam)
        for j in range(len(szam_str)):  
            ossz += int(szam_str[j])
        szam = ossz
    összeg.append(szam)

a = 0

for i in range(kerdesek_szama):
    hossz = veg[i] - kezd[i] + 1
    print(sum(összeg[a:a + hossz]))
    a += hossz
