def HányPáros(t):
    db = 0
    for i in range(0,len(t)):
        if t[i]%2 == 0:
            db = db+1
            
    return db

print(f'{HányPáros([5,2,6,8,3,6])}')

