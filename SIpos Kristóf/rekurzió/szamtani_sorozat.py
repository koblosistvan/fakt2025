def szamtsorozat(a1,d,n):
    if n==1:
        return a1
    else:
        return szamtsorozat(a1,d,n-1)+d

print(szamtsorozat(91,4,67))

