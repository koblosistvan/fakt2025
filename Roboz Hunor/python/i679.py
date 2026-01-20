a = input().split()
növény, térfogat=int(a[0]),int(a[1])

locsolt = []

viz = input().split()

for i in range(növény):
    locsolt.append(int(viz[i]))
    
átlag = round(sum(locsolt)/len(locsolt))
ind_á = ''
darab_á = 0

for i in range(len(locsolt)):
    if átlag == locsolt[i]:
        ind_á += f'{str(i)} '        
        darab_á += 1
        
if darab_á == 0: 
    ind_á = -1

index_á= ''
if ind_á != -1:
    for i in range(len(ind_á)):
        if ind_á[i] != ' ':
            index_á += ind_á[i]
        else:
            break
else: index_á = ind_á           
index_á = int(index_á)

print(f'{átlag} {index_á+1} {darab_á}')


max_darab = 0
modus = -1

for i in range(len(locsolt)):
    darab = 0
    for j in range(len(locsolt)):
        if locsolt[i] == locsolt[j]:
            darab += 1

    if darab > max_darab:
        max_darab = darab
        modus = locsolt[i]

if max_darab == 1:
    modus = -1


ind_mo = ''
darab_mo = 0

for i in range(len(locsolt)):
    if modus == locsolt[i]:
        ind_mo += f'{str(i)} '        
        darab_mo += 1
        
if darab_mo == 0: 
    ind_mo = -1
    
index_mo= ''
if ind_mo != -1:
    for i in range(len(ind_mo)):
        if ind_mo[i] != ' ':
            index_mo += ind_mo[i]
        else:
            break
else: index_mo = ind_mo           
index_mo = int(index_mo)
    
    
print(f'{modus} {index_mo+1} {darab_mo}')    
    
    
    
'''for i in range(len(locsolt)):
    for j in range(len(locsolt)-i-1):
        if locsolt[j] > locsolt[j+1]:
            locsolt[j],locsolt[j+1] = locsolt[j+1],locsolt[j]
            '''

rend = sorted(locsolt)

if len(locsolt) % 2 == 1:
    median = rend[len(locsolt) // 2]
else:
    median = (rend[len(locsolt) // 2 - 1] + rend[len(locsolt) // 2]) / 2


ind_me = ''
darab_me = 0

for i in range(len(locsolt)):
    if median == locsolt[i]:
        ind_me += f'{str(i)} '        
        darab_me += 1
        
if darab_me == 0: 
    ind_me = -1
    
index_me= ''
if ind_me != -1:
    for i in range(len(ind_me)):
        if ind_me[i] != ' ':
            index_me += ind_me[i]
        else:
            break
else: index_me = ind_me           
index_me = int(index_me)

print(f'{median} {index_me+1} {darab_me}')    