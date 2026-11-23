def legnagyobb_közös_osztó(a,b):
    if a==b:
        return a
    else:
        if a>b:
            a,b=b,a
        print(f'({a},{b-a})= ')
        return legnagyobb_közös_osztó(a,b-a)


print('(67, 895467)= ')
print(legnagyobb_közös_osztó(67, 8967))
