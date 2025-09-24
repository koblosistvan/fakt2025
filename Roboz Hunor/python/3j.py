a = int(input('adj meg egy számot: '))
eredmény = ''
rendsz = int(input('Válassz számrandszert: '))
while a > 0 :
   maradek = a % rendsz
   eredmény = str(maradek) + eredmény
   a = (a - maradek) // rendsz
   
print(eredmény)


