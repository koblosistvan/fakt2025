import random
m = []
for i in range(10):
    a = random.randint(-5,3)
    m.append(a)
alatt = 0
rajta = 0
for i in range(len(m)):
    if m[i] == 0:
        rajta+=1
    elif m[i] <0:
        alatt+=1
print(f'A delfin a víz alatt az út {round(alatt/80*100)}%-át a víz felszínén pedig az út {round(rajta/80*100)}%-át')

a =0
b = 0
for i in range(len(m)):
    if m[i] > 0:
        a+=1
    elif m[i] <0:
        b+=1
if a > b:
    print('A delfin a víz felett többett volt')
elif a < b:
    
    print('A delfin a víz alatt többett volt')
else:
    print('A delfin ugyanannyit volt a víz felett mint alatt')

hossz = 0

index = 0
h = 0
for i in range(len(m)-1):
    
    if m[i] and m[i+1] > 0:
        h += 2
    elif m[i] > 0:
        h += 1
    else: h=0
if h > hossz :
        hossz = h
        index = i
print(f'A leghosszabb idejű kiugrása {hossz} alkalomig volt')

á = 0
for i in range(len(m)-1):
    if m[i] < 0 and m[i+1] > 0:
        á+=1
print(f'{á} alkalommal törte át a felszínt')

