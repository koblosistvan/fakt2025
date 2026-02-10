hőmérséklet=float(input('Add meg a hőmérsékletet: '))
if hőmérséklet <= 0:
    print('Szilárd')
elif 100>hőmérséklet>0:
    print('Folyékony') 
elif hőmérséklet>=100:
    print('gáz')