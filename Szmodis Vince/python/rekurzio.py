def szamjegyek_osszege(n):
    if n<10:
        return n
    else:    
        return n%10+szamjegyek_osszege(n//10)
    

print(szamjegyek_osszege(99))
