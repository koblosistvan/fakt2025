import random
import os
os.system("cls")
c = random.randint(100000,100000000000000)
d = random.randint(100000,100000000000000)
def lnko(a, b):
    if a == b:
        return a
    else:
        if a > b:
            a, b = b, a
    return(lnko(a, b-a))


print(lnko(c, d))
