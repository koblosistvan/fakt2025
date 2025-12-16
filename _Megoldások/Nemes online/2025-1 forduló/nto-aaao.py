bemenet = 'MaganhangzokAngolNyelven'

maganhangzok = 'aeiouy'
for c in bemenet:
    if c.lower() in maganhangzok:
        print(c, end='')

print()
