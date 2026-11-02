t = []
def hanyparos(t):
    db = 0
    for i in range(len(t)):
        if t[i]%2 == 0:
            db = db+1
    return db

print(hanyparos([5, 2, 6, 8, 3, 6]))