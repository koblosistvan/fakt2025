import math
import random 
oszt =['dobai', 'Artúr','hunor', 'boróka', 'csilla','bp','bercel','panna', 'Zeti','bendi','Anna','Hanna','Dani','Ballabas','Peti','Vivi', 'sarolta','Sara','Bibor','Adam']
letszam = len(oszt)
opció = oszt.copy()
parok = []


while len(oszt) != 0:
    par = '\n'
    akt = random.choice(opció)
    if akt == oszt[0]:
        akt = random.choice(opció)
    par += f'{oszt[0]} - {akt}'
    parok.append(par)
    opció.remove(akt)
    oszt.remove(oszt[0])
    
print(*parok)