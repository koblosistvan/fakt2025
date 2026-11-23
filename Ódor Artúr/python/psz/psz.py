def hany_paros(t):
    db = 0
    for i in range(len(t)):
        if t[i] % 2 == 0:
            db +=1
    print(db)
paros([2,3,4,6])