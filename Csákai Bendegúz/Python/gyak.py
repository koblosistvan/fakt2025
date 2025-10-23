sz = int(input('Add meg a szélességet: '))
m = int(input('Add meg a magasságot: '))
for y in range(m):
    for x in range(sz):
        print('*', end='')
    print()

print('\n','-' * sz * 2, '\n')

for x in range(sz):
    for y in range(x+1):
        print('x', end='')
    print()

print('\n' + '-' * sz * 2 + '\n')

for x in range(sz):
    for y in range(x):
        print(' ', end='')
    for y in range(sz-x):
        print('*', end='')
    print()

for x in range(sz):
    for y in range(x):
        print('*', end='')
    for y in range(sz-x):
        print(' ', end='')
    print()

print('\n' + '-' * sz * 2 + '\n')

for x in range(sz):
    for y in range(x+1):
        print('*', end='')
    print()