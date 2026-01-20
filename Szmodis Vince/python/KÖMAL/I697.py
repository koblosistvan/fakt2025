forras=[11, 100,
48 ,15, 18 ,18, 15, 18 ,8 ,15, 11, 18, 10
]

novenyek_szama=forras[0]
viz_max_terfogat=forras[1]
locsolt_egyenkent=forras[2:]


osszeg=0
for i in range(novenyek_szama):
    osszeg+=locsolt_egyenkent[i]
    
atlag_locs=round(osszeg//novenyek_szama)

atlag_locs_index=0
for i in range(novenyek_szama):
    if locsolt_egyenkent[i]==atlag_locs:
        atlag_locs_index=i
        
atlag_locs_osszes=0
for i in range(novenyek_szama):
    if locsolt_egyenkent[i]==atlag_locs:
        atlag_locs_osszes+=1

modusz=locsolt_egyenkent[0]
modusz_db=0
proba=0
proba_db=0
for i in range(novenyek_szama):
    if modusz==locsolt_egyenkent[i]:
        modusz_db+=1
    elif modusz!=locsolt_egyenkent[i]:
        proba=locsolt_egyenkent[i]
        proba_db+=1
        if modusz_db<proba_db:
            modusz=proba
            proba=0
            proba_db=0

modusz_index=0
for i in range(novenyek_szama):
    if locsolt_egyenkent==modusz:
        modusz_index=i
        break

modusz_osszes=0
for i in range(novenyek_szama):
    if locsolt_egyenkent==modusz:
        modusz_osszes+=1

for i in range(novenyek_szama):
    for j in range(novenyek_szama-i-1):
        if locsolt_egyenkent[j]>locsolt_egyenkent[j+1]:
            locsolt_egyenkent[j],locsolt_egyenkent[j+1]=locsolt_egyenkent[j+1],locsolt_egyenkent[j]

median=0
if novenyek_szama % 2==1:
    median=locsolt_egyenkent[novenyek_szama//2]
else:
    median_atlag = locsolt_egyenkent[novenyek_szama/2]+locsolt_egyenkent[novenyek_szama/2+1]
    if median_atlag-locsolt_egyenkent[novenyek_szama/2]<locsolt_egyenkent[novenyek_szama/2+1]-median_atlag:
        median= locsolt_egyenkent[novenyek_szama/2]
    else:
        median=locsolt_egyenkent[novenyek_szama/2+1]

median_index=0
for i in range(novenyek_szama):
    if locsolt_egyenkent[i]==median:
        median_index=i
        break

median_osszes=0
for i in range(novenyek_szama):
    if locsolt_egyenkent[i]==median:
        median_osszes+=1

print(f'{atlag_locs} {atlag_locs_index} {atlag_locs_osszes}\n{modusz} {modusz_index} {modusz_osszes}\n{median} {median_index} {median_osszes}')



