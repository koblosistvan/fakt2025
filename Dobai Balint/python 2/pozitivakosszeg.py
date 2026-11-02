'''
eljaras osszeg (T(1,n))
    S := 0
    Ciklus i = 1-től n-ig
        Ha T(i) pozitív, akkor
            T(i) := S:
    Ciklus vége
    ki : S


'''

def pozosszeg(t):
    osszeg = 0
    for i in range(1,len(t)):
        if t(i) % 2 ==0:
            