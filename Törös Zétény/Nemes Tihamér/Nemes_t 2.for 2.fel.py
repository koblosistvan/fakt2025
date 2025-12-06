gol = int(input())
golok = []
for i in range(gol):
    golok.append(int(input()))
legnagyobb = 0
x = 0
a = 0
b = 0
dontetlen = 1
for i in range(gol):
    if golok[i] == 1:
        a += 1
    else:
        b += 1
    if a == b:
        dontetlen += 1
'''
    if a > b:
        while golok[i] != 1:
            x += 1
            if legnagyobb < x:
                legnagyobb = x
        else: 
            x = 0
    elif a < b:
        while golok[i] != 2:
            x += 1
            if legnagyobb < x:
                legnagyobb = x
        else: 
            x = 0
'''
print(a,  b)
print(dontetlen)
#print(legnagyobb)
