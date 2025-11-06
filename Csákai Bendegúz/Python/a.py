import random
ossz = 0
s = ""

while True:
    a = random.randint(0,10)
    if a == 0:
        a= str(a)
        s += (f'{a}')
        break
    else:
        if a % 2 == 1:
           ossz += a
        a= str(a)
        s += (f'{a}, ')
    
print(f'{s} A páratlanok összege: {ossz}')