import timeit

def hatvany_rekurziv(a, n):
    if n == 1:
        return a
    elif n%2 == 0:
        return hatvany_rekurziv(a, n//2) ** 2
    else:
        return a * hatvany_rekurziv(a, n-1)

def hatvany(a, n):
    p = 1
    for i in range(n):
        p *= a
    return p


print(timeit.timeit('hatvany_rekurziv(2, 1000)'))
print(timeit.timeit(hatvany(2, 1000)))
