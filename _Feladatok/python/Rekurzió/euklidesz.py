def lnko(a, b):
    if a == b:
        return a
    else:
        # ha b kisebb, akkor cserélünk
        if a > b:
            a, b = b, a
        print(f'({a}, {b-a}) = ')
        return lnko(a, b-a)

a, b = 5845, 12325
print(f'({a}, {b}) = ')
print(lnko(a, b))

    
        