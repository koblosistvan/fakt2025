def lepcso(a):
    if a == 1:
        return 1
    else:
        return a+lepcso(a-1)
print(lepcso(100))