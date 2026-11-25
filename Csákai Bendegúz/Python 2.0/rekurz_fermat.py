def fermat(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    if n%2 == 0:
        return fermat(a, n/2)**2
    if n%2 != 0:
        return fermat(a,n-1)**2*a

print(fermat(4,5))