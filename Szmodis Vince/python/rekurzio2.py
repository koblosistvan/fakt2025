def binomialis(n, k):
    if n == 1 or k==0:
        return 1
    else:
        return binomialis(n-1, k)+binomialis(n-1, k-1)

print(binomialis(12, 1))