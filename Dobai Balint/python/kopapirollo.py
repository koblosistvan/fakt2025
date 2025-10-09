import random

mutatas = []

te_pontod = 0
gep_pontja = 0

tied = str(input('valassz egyet ko papir es ollo kozul: '))


for i in range(3):
    mutatas.append (random.randint (1,3))

if mutatas == 1:
    mutatas = 'ko'
elif mutatas == 2:
    mutatas = 'papir'
else:
    mutatas == 3
    mutatas = 'ollo'

if tied == 'ko' and mutatas == 'papir' or tied == 'papir' and mutatas == 'ollo' or tied == 'ollo' and mutatas == 'ko':
    print('vesztettel')
    gep_pontja +=1


if tied == 'ko' and mutatas == 'ollo' or tied == 'papir' and mutatas == 'ko' or tied == 'ollo' and mutatas == 'papir':
    print('nyertel')
    te_pontod +=1


if tied == mutatas:
    te_pontod +=1
    gep_pontja +=1



print(f'a gep ezt mutatta {mutatas}')
print(te_pontod)
print(gep_pontja)





