'''
    n!
k!*(n-k)!

'''
def binom(n,k):
    if n == k or k == 0:
        return 1
    else:
        return binom(n-1,k)+binom(n-1,k-1)
print(binom(12, 2))


