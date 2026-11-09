import random
dobások = []
for i in range(100):
    dobások.append(random.randint(1,6))
print(dobások)

hatosokszama=0
for i in range (len(dobások)):
    if dobások[i] == 6:
        hatosokszama +=1
print(f'a dobások között {hatosokszama} hatos volt. ')

parosok_szama=0
páratllanok_száma=0
for i in range(len(dobások)):
    if dobások[i] % 2 ==0:
        parosok_szama +=1

    


    else:
        páratllanok_száma+=1
print(f'Párosok száma {páratllanok_száma}')
print(f'Párosok száma {parosok_szama}')

egy_ketto=0
for i in range(len(dobások)-1):
    if dobások[i] == 1 and dobások [i+1] ==2:

    
        egy_ketto+=1

print(egy_ketto)

nagyobb=0

for i in range(len(dobások)-1):
    if dobások[i] > dobások[i+1]:
        nagyobb+=1

print(nagyobb)


szamlalok=[0,0,0,0,0,0]
for i in range(len(dobások)):
    szamlalok[dobások[i]-1]+=1

print(szamlalok)

print('Dobások:')
for i in range(1,7):
    print(f'\t{i} {szamlalok[i-1]}')
