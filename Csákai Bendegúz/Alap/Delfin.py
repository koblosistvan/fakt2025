import random
mag = []
legn_kiug = 10
for i in range(legn_kiug):
    mag.append(random.randint(-5,3))
print(mag)
ugras = 0
vizfelsz = 0
vizalatt = 0
for i in range(legn_kiug):
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
for i in range(legn_kiug):
    if szazal_ugr > szazal_vizal:
        print('A víz felett volt többet a delfin')
        break
else:
    print('A víz alatt volt többet a delfin')
#Milyen hosszú volt a leghosszabb kiugrása? Az út hányadik pontjánál kezdődött?
hossz = 0
legn_hossz = 0
legn_hossz_index = 0
for i in range(legn_kiug):
    if mag[i] > 0:
        hossz += 1
    else:
        if hossz > legn_hossz:
            legn_hossz = hossz
            legn_hossz_index = i-legn_hossz+1
        hossz = 0
print(f'A leghosszabb kiugrás {legn_hossz} hosszú volt, és a {legn_hossz_index}-nál/nél kezdődött')
attor = 0
for i in range(legn_kiug):
    if mag[i-1]*mag[i] < 0:
        attor +=1
print(f'{attor}x törte át a felszínt')

mélymer = [-4, -5]
mélymerdb = 0
for i in range(legn_kiug):
    if (mag[i] in mélymer) and (mag[i-1]*mag[i] != 16 or mag[i-1]*mag[i] != 20 or mag[i-1]*mag[i] != 25):
        mélymerdb += 1
print(f'{mélymerdb}x volt mélymerülésben')

