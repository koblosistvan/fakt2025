def lepcso(n):
    if n == 1:
        return 1
    else:
        return n + lepcso(n-1)    

print(lepcso(200))

def faktorialis (n):
    if n == 1:
        return 1
    else:
        return n*faktorialis(n-1)

print(faktorialis(5))

def szamjegyossz (n):
    if n < 10:
        return n
    else:
        return n % 10 + szamjegyossz(n//10)

def binomialis(n, k):
    if n == k or k ==0:
        return 1
    else:
        return binomialis(n-1,k) + binomialis(n-1,k-1)

print(binomialis(12,7))

def szamtani(a1, d , n):
    if n == 1:
        return a1
    else:
        return szamtani(a1,d,n-1) + d

print(szamtani(91,4,67))

def mertani(a1,q,n):
    if n == 1:
        return a1
    else:
        return mertani (a1,q,n-1) * q
print(mertani(91,4,67))
    

        




