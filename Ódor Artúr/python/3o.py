x = 0
y = 0
szamlalo = 0



while szamlalo != 1000:    
    for i in range(szamlalo):
        y = szamlalo * -1
        x = 0
        x -= 1
        y += 1

        if 3*x + 4*y == 52:
            print(x, y)

    szamlalo += 1