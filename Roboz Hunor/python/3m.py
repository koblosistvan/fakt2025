a = int(input('Milyen széles legyen? '))
b = int(input('Milyen magas legyen? '))

for y in range(b):
    for x in range(a):
        if (x + y) % 2 ==0:
            print('█', end = '')
        else:
            print(' ', end = '')
    print()



print('\n' + '-' *80 +'\n')





for y in range(b):
    for x in range(y+1):
        print('o', end = '')
    print()


print('\n' + '-' * 80+'\n')


for y in range(b):
    for x in range(y):
        print(' ', end = '')
    for x in range(a-y):
        print('o', end = '')
    print()


for y in range(b):
    for x in range(x-2*y):
        print('o', end = '')



