import random

ut = []
for i in range(80):
    ut.append(random.randint(-5,3))

vizben = 0
viz_alatt = 0
viz_felett = 0
ossz = len(ut)
for i in range(len(ut)):
    if ut[i] ==0:
        vizben +=1
    if ut[i] > 0:
        viz_felett +=1
    if ut[i] < 0:
        viz_alatt +=1

print(f"\nA delfin az út {vizben/ossz:.2%}-át töltötte a vízfelszínen.")
print(f"A delfin az út {viz_alatt/ossz:.2%}-át töltötte a víz alatt.")
print(f"A delfin az út {viz_felett/ossz:.2%}-át töltötte a víz felett.")


if viz_alatt > viz_felett:
    print("A delfin többet volt a víz alatt.")
elif viz_felett > viz_alatt:
    print("A delfin többet volt a víz felett.")
else:
    print("A delfin ugyanannyit volt a víz alatt és felett.")


max_hossz = 0
akt_hossz = 0
max_kezd = 0

for i in range(len(ut)):
    if ut[i] > 0:
        akt_hossz += 1
        if akt_hossz > max_hossz:
            max_hossz = akt_hossz
            max_kezd = i - akt_hossz + 1
    else:
        akt_hossz = 0

print(f"A leghosszabb kiugrás hossza: {max_hossz}")
print(f"A kiugrás a(z) {max_kezd + 1}. pontnál kezdődött.")


attoresek = 0
for i in range(1, len(ut)):
    if ut[i-1] * ut[i] < 0:
        attoresek += 1

print(f"A delfin {attoresek} alkalommal törte át a vízfelszínt.")


mely_merulesek = 0
melysegben = False

for asd in ut:
    if asd in (-4, -5):
        if not melysegben:
            mely_merulesek += 1
            melysegben = True
    else:
        melysegben = False

print(f"A delfin {mely_merulesek} alkalommal merült mélyre.")
