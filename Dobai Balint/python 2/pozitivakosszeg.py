'''
eljaras osszeg (T(1,n))
    S := 0
    Ciklus i = 1-től n-ig
        Ha T(i) pozitív, akkor
            T(i) := S:
    Ciklus vége
    ki : S
'''
'''
def pozosszeg(t):
    osszeg = 0
    for i in range(1,len(t)):
        if t(i) > 0:
            s += t(i)
    print(s)
'''
def eloallitas (a,b,s):
    SA = []
    SB = []
    i=0
    j =0
    for i in range(len(s)):
        if A >=s[i]:
            SA.append(s[i])
            i +=1
            A -=s[i]
        elif B >= s[i]:
            SB.append(s[j])
            j+=1
            B -= s[i]

        
        




