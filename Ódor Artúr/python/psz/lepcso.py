def lepcso(n):
    if n == 1:
        return 1
    else:
        return n + lepcso(n-1)
print(lepcso(5))