a = int(input('adj meg egy számot'))
b = int(input('adj meg egy számot'))

if a > b:
    if a % b ==0:
        print(f'{a} osztható {b}-vel')
    else:
        print(f'{a} nem osztható {b}-vel')
elif a == b:
    print('A két szám egyenlő')
else:
    if b % a == 0:
        print(f'{b} osztható {a}-vel')
    else:
        print(f'{b} nem osztható {a}-vel')
