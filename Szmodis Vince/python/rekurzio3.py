def szamtani(a1, d, n):
    if n==1:
        return a1
    else:
        return szamtani(a1, d, n-1) + d

print(szamtani(1,5,2))