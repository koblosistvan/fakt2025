def hatvany(a,n):
    if n==1:
        return a
    elif a%2 ==0:
        n/2=n
        return hatvany()
    else:
        a*a**n-1
        return hatvany()

