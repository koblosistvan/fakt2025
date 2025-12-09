db = int(input())
gol = []
for i in range(db):
    a = int(input())
    gol.append(a)
hazai,vendeg,döntetlen,leg,utolso,sorozat,kezdo_h,kezdo_v = 0,0,1,0,0,0,0,0,
for i in range(len(gol)):
    elozo_h,elozo_v = hazai,vendeg
    
    if gol[i] == 1:
        hazai +=1
    else:vendeg+=1
    
    if vendeg == hazai:
        döntetlen+=1
        
    if gol[i] == utolso:
        sorozat+=1
    else:
        utolso = gol[i]
        sorozat = 1
        kezdo_h,kezdo_v = elozo_h,elozo_v
        
    if gol[i] == 1 and hazai > vendeg and kezdo_h < kezdo_v:
            if sorozat > leg:
                leg = sorozat
    if gol[i] == 2 and hazai < vendeg and kezdo_h > kezdo_v:
        if sorozat > leg:
                leg = sorozat
    
print(f'{hazai} {vendeg}\n{döntetlen}\n{leg}')

