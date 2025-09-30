sz = int(input('széleség: '))
m = int(input('magasság: '))

for y in range(m):
    for x in range(sz):
        if (x + y) % 2 == 0:
            print('█', end='')
        else:
            print(' ', end='')
    print()

print('\n' + '-'* 80 + '\n')

for y in range(sz):
    for x in range(y+1):
        print('█', end='')
    print()

print('\n' + '-'* 80 + '\n')

for y in range(sz):
    for x in range(y):          # y - szor
        print(' ', end='')
    for x in range(sz-y):       # sz - y -szor
        print('█', end='')      # összesen: sz-szer
    print()

print('\n' + '-'* 80 + '\n')


