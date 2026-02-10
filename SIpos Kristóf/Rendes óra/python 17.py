import random
szám=random.randint(1,100)
tipp=int(input('tippelj egy számot: '))
while tipp!=szám:
    tipp=int(input('tippelj egy számot: '))
print('ügyes vagy')