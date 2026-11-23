def szjossz(n):
    if n < 10:
        return n
    else:
        return n%10 + szjossz(n//10)
        