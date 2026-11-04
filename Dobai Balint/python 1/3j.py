szam = int(input('adj meg egy szamot'))
alap = int(input('add meg a szamrendszert'))
eredmeny = ''
while szam > 0:
    maradek = szam % alap
    eredmeny = str(maradek) + eredmeny
    szam = (szam-maradek) //alap
        
    

print(f'a megadott szamrendszerben:{eredmeny}')