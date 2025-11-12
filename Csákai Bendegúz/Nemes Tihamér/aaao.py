s="aeiouyAEIOUY"
mg=str(input('Adj meg egy szót: '))
mgszm=""
for c in mg:
    if c in s:
        mgszm += c
print(mgszm)