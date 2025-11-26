import random
Euro=382 #FT
Y_or_N=random.randint(1,2)
if Y_or_N == 1:
    money=random.randint(1,4)
    if money==1:
        print(f'Feltölthetsz 5€-t és az {Euro*5} FT-ba fog kerülni. 5€ nem sok de néha pont elég.')
    elif money==2:
        print(f'Feltölthetsz 10€-t és az {Euro*10} FT-ba fog kerülni. 10€ az kb jó nem túl drága és pár dologra kitelik belőle.')
    elif money==3:
        print(f'Feltölthetsz 25€-t és az {Euro*25} FT-ba fog kerülni. 25€ kicsit kezd borsos lenni de cserébe rengeteg dolgot tudsz venni.')
    elif money==4:
        print(f'Feltölthetsz 50€-t és az {Euro*50} FT-ba fog kerülni. 50€ ??? Csávó csöves leszel.')
else:
    print('Több pénz fog maradni most a számládon.')