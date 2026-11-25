def hatvanyozas(a, n):
    if n == 1:
        return a
    else:
        if n % 2 == 0:
            return hatvanyozas(a, n/2)
        else:
            n % 2 == 1
            return hatvanyozas(a, (n-1)/2)

