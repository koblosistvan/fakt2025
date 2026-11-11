def szamossz(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return n%10 + szamossz(n//10)
print(szamossz(3253))
