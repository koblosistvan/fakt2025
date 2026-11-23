def csik():
    print('-'*40)

def lepcso(n):
    if n == 1:
        return 1
    else:
        return n + lepcso(n-1)

print(lepcso(200))
csik()

def szamjegyek_osszege(n):
    if n < 10:
        return n
    else:
        return n%10 + szamjegyek_osszege(n//10)

print(szamjegyek_osszege(65345276))
print(szamjegyek_osszege(65))
print(szamjegyek_osszege(9))
print(szamjegyek_osszege(-456))
csik()


def binom(n, k):
    if n == k or k == 0:
        return 1
    else:
        return binom(n-1, k) + binom(n-1, k-1)

print(binom(14, 5))
csik()


def szamtani(a1, d, n):
    if n == 1:
        return a1
    else:
        return szamtani(a1, d, n-1) + d
print(szamtani(1, 5, 2))
csik()