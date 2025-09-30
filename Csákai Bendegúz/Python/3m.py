sz = int(input('Szélesség: '))
m = int(input('Magasság: '))
for y in range(m):
    for x in range(sz):
        if (x + y) % 2 == 0:
            print('█', end='')
        else:
            print(' ', end='')
    print()

print('\n' + '-' * sz + '\n')

for x in range(sz): 
    for y in range(x+1):
        print('x', end='')
    print()

print('\n' + '-' * sz + '\n')

for x in range(sz): 
    for y in range(x):
        print(' ', end='')
    for y in range(sz-x):
        print('x', end='')
    print()

print('\n' + '-' * sz*2 + '\n')

for x in range(sz): 
    for y in range(x):
        print(' ', end='')
    for y in range(sz-2*x):
        print('x', end='')
    print()