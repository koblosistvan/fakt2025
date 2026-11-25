def szamjegyek_osszege(n):
    if n<10:
        return n
    else:
        return n%10 + szamjegyek_osszege(n//10)
    
"""print(szamjegyek_osszege(-2134))"""

def binomialis(n,k):
    if n == k or k == 0:
        return 1
    else:
        return binomialis(n - 1, k) + binomialis(n - 1, k - 1)

"""print(binomialis(5, 3))"""

def szamtani(a1, d, n):
    if n == 1:
        return a1
    else:
        return szamtani(a1, d, n-1) + d

"""print(szamtani(91, 4, 670))"""

def mertani(a1, d, n):
    if n == 1:
        return a1
    else:
        return mertani(a1, d, n-1) * d

"""print(mertani(6,7,67))"""