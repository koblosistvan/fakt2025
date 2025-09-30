sz = int(input('szélesség: '))
m = int(input('magasság: '))

for y in range (m):
    for x in range(sz):
        if  (x+y) % 2 == 0:
            print('█',end='')
        else:
            print(' ',end='')
    print()

sz2 = int(input('háromszög nagysága: '))


for y in range(sz2):
    for x in range (y+1):
        print('█',end='')
    print()

for y in range(sz2):
    for x in range(y):
        print(' ',end='')
    for x in range (sz2-y):
        print ('█', end='')
    print()