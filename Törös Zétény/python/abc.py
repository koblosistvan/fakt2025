def szamjegyek_osszege(n):
    if n < 10:
        return n
    else:
        return n%10 + szamjegyek_osszege(n//10)

print(szamjegyek_osszege(623482))

def binom(n, k):
    if n==k or k == 0:
        return 1
    else:
        return binom(n-1, k)+binom(n-1, k-1)


print(binom(12, 8))

def szamtani(a1, d, n):
    if n == 1:
        return a1
    else:
        return szamtani(a1, d, n-1) + d

print(szamtani(7, 8, 4))

def mertani(b1, c, f):
    if f == 1:
        return b1
    else:
        return 