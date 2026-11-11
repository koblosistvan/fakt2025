def lepcso(n):
    if n == 1:
        return 1
    else:
        return n+lepcso(n-1)

print(lepcso(100))

def faktorialis(n):
    if n == 0:
        return 1
    else:
        return n*faktorialis(n-1)
print(faktorialis(7))