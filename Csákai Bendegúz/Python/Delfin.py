import random
mag = []
hossz = 10
for i in range(hossz):
    mag.append(random.randint(-5,3))
print(mag)
ugras = 0
vizfelsz = 0
vizalatt = 0
for i in range(hossz):
    if mag[i] > 0:
        ugras += 1
    elif mag[i] == 0:
        vizfelsz += 1
    else:
        vizalatt += 1
szazal_ugr = ugras/80*100
szazal_vizf = vizfelsz/80*100
szazal_vizal = vizalatt/80*100
print(f'A delfin az út {szazal_vizf:.0f}%-át tette meg a vízfelszínen, az út {szazal_vizal:.0f}%-át tette meg a víz alatt, így összesen az út {szazal_vizal+szazal_vizf}% át tette meg vízben (kerekítve!!)')
for i in range(hossz):
    if szazal_ugr > szazal_vizal:
        print('A víz felett volt többet a delfin')
        break
else:
    print('A víz alatt volt többet a delfin')
attor = 0
for i in range(hossz):
    if mag[i-1]*mag[i] < 0:
        attor +=1
print(f'{attor}x törte át a felszínt')
mélymer = [-4, -5]
mélymerdb = 0
for i in range(hossz):
    if (mag[i] in mélymer) and (mag[i-1]*mag[i] != 20 or mag[i-1]*mag[i] != 25):
        mélymerdb += 1
print(f'{mélymerdb}x volt mélymerülésben')

