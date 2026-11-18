def mertani(a1, q, n):
    if n ==1:
        return a1
    else:
        return mertani(a1, q, n-1)*q