'''def szamjegyek_osszege(n):
    if n < 10:
        return n
    else:
        return n % 10 + szamjegyek_osszege(n//10)
print(szamjegyek_osszege(226))
'''


'''def binomialis(n,k):
    if n == k or k == 0:
        return 1
    else:
        return binomialis(n-1,k) + binomialis(n-1,k-1)
print(binomialis(7,6))
'''


'''
def szamtani(a1,d,n):
    if  n == 1:
        return a1
    else:
        return szamtani(a1,d,n-1)+d

print(szamtani(2,3,67))
'''

'''
def mertani(a1,q,n):
    if  n == 1:
            return a1
    else:
        return mertani(a1,q,n-1)*q
    
print(mertani(2,3,67))
'''


'''
def lnko(a,b):
    if a == b:
        return a
    else:
        if a > b:
            a, b = b, a
        return lnko(a,b-a)
print(lnko(9,21))
'''


def valami(a,n):
    if n == 1:
        return
    else:
        if n % 2 == 0:
            return valami(a,n/2)**2
        else:
            return valami(a-1,n/2)**2*a

print(valami(3,4))


