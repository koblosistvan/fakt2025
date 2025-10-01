import random 
jeles = 96
erettsegi = []
erettsegi_db = 20
maxpont = 120 

for i in range(erettsegi_db):
    pontszam = random.randint(1,120)
    erettsegi.append(pontszam)

harompontnalkevesebb = 0 

for i in range(erettsegi_db):
    if erettsegi[i] < 96 and erettsegi[i] >=jeles-3:
        harompontnalkevesebb +=1

maxpontos = 0

for i in range(erettsegi_db):
    if erettsegi[i] == maxpont:
        maxpontos += 1


savok = [0] * 10
for i in erettsegi:
    hely = min(i // 12,9)
    savok[hely] += 1


for i in range(erettsegi_db):
    atlag = sum(erettsegi) // erettsegi_db

print(f'{harompontnalkevesebb} erettsegi lett majdnem jeles')
print(f'{maxpontos} erettsegi lett max pontos')
print(f'{atlag} lett erettsegik átlaga')
print("10%-os sávok (0-11, 12-23, ..., 108-120):")

sáv_kezd = 0
sáv_vég = 11

for sáv_db in savok:
    print(sáv_kezd, "-", sáv_vég, ":", sáv_db, "fő")
    if sáv_vég == 107:
        sáv_vég +=13
        sáv_kezd +=12
    else:
        sáv_kezd += 12
        sáv_vég += 12

