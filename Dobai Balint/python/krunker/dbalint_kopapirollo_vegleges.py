import random

lehetoseg = ['ko', 'papir', 'ollo']
te_pontod = 0
gep_pontja = 0

for kor in range(1, 4):  
    while True:
        tied = input(f"{kor}. kor.  valassz: ko, papir vagy ollo: ")
        if tied in lehetoseg:
            break
        print("ervenytelen bemenet valassz ko, papir vagy ollo kozul")
    
    mutatas = random.choice(lehetoseg)
    print(f"a gep ezt valasztotta {mutatas}")

    if tied == mutatas:
        print("dontetlen, 1-1 pont jar")
        te_pontod +=1
        gep_pontja +=1
    elif (tied == 'ko' and mutatas == 'ollo') or (tied == 'papir' and mutatas == 'ko') or (tied == 'ollo' and mutatas == 'papir'):
        print("Nyertél ezen a körön!\n")
        te_pontod += 1
    else:
        print("A gép nyert ezen a körön.\n")
        gep_pontja += 1

    print(f"Jelenlegi pontok: Te {te_pontod} - GéP {gep_pontja}\n")

print(f"Te: {te_pontod}  GéP: {gep_pontja}")
if te_pontod > gep_pontja:
    print("nyertel")
elif te_pontod < gep_pontja:
    print("vesztettel.")
else:
    print("dontetlen lett")
