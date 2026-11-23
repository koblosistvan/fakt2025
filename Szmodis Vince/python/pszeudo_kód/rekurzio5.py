def euklidesz(a,b):
    if a == b:
        return a
    else:
        if a>b:
            a, b = b, a
        
        return euklidesz(a, b-a)

print(euklidesz(2222, 13722))

