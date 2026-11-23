def binegyuthato(n,k):
    if n == k or k==0:
        return 1
    else:
        return binegyuthato(n-1,k)+binegyuthato(n-1,k-1)

print(binegyuthato(12,1))