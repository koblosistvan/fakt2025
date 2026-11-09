def hanyparos(t):
    t=[5, 2, 6, 8, 3, 6]
    db=0
    for i in range(0, len(t)):
        if t[i]%2==0:
            db+=1

    print(db)
