def mertsorozat(a1,q,n):
    if n == 1:
        return a1
    else:
        return mertsorozat(a1,q,n-1)*q

print(mertsorozat(6,8,13))