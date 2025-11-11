import random

magassag = []
for i in range(80):
    magassag.append(random.randint(-5,3))

print(magassag)

viz_alatt = magassag[0]
viz_alatt_index = 0
viz_felett = magassag[0]
viz_felett_index = 0
viz_felszine = magassag[0]
viz_felszine_index = 0
for i in range (len(magassag)):
    if magassag[i] > 0:
        viz_felett_index += 1

for i in range (len(magassag)):
    if magassag[i] < 0:
        viz_alatt_index +=1


a= viz_felett_index / len(magassag)
b= viz_alatt_index / len(magassag)


print(f'a viz felett toltott ido az egesznek {a*100} % resze')
print(f'a viz alatt toltott ido az egesznek {b*100} % resze')


for i in range(len(magassag)):
    if viz_felett_index > viz_alatt_index:
        print(f'a viz felett tobbett toltott ami {a} volt')        
        break
else: viz_alatt_index > viz_felett_index
print(f'a viz felett tobbet toltott ami {b*100} % volt')

mely_merules = magassag[0]
mely_merules_index = 0


for i in range(len(magassag)):
    if magassag[i] == -4 or magassag == -5:
        mely_merules_index +=1

print(f'mely merules {mely_merules_index}-szer volt')




