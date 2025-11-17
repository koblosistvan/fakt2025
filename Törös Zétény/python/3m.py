w = int(input('Szélesség: '))
l = int(input('Magasság: '))

for y in range(l):
    for x in range (w):
        if (x+y) % 2 == 0:
            print(' ', end='')
        else:
            print('█', end='')
    print()

sz = int(input('Mekkora legyen a háromszög: '))

for i in range (sz):
    for x in range (i+1):
        print('█', end='')
    print()

print('')

for y in range(sz):
    for x in range(y):
        print(' ', end='')
    for x in range(sz-y):
        print('█', end='')
    print()








































67