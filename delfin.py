import random
ugras = []
u = 80
for i in range(u):
    ugras.append(random.randint(-5,3))
print(ugras)
felszinen =0
alatta=0
felette=0
for i in range(u):
    if ugras[i] == 0:felszinen+=1
    elif ugras[i]<0:alatta+=1
    else:felette+=1
print(f'A víz felszínen az út {felszinen/u*100:.0f}%-át tette, míg alatta az út {alatta/u*100:.0f}%-át')
if alatta < felette: print('A delfin a víz felett volt többet')
elif alatta > felette: print('A delfin a víz alatt volt többet')
else: print('A delfin ugyanannyit volt a víz alatt mint felett')
h =0
H=0
index=0
for i in range(u):
    if ugras[i] > 0:
        h+=1
    else:
        if H < h:
            H=h
            index=i-H+1
        h =0
print(f'A leghoszabb ugrás {H} hosszú volt és {index} ugrásnál kezdődött')
á =0
for i in range(u-1):
    if ugras[i] < 0 and ugras[i+1]>0 or ugras[i] > 0 and ugras[i+1]<0:
        á+=1
print(f'{á} alkalommal törte át a felszínt')

m = 0
for i in range(u-1):
    if ugras[i]<=-4 and ugras[i+1] >-4:
        m+=1
print(f'{m}szer merült mélyre')