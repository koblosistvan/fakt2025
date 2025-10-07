
n = int(input("Szám: "))
a = int(input("Számrendszer: "))

out = ""

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n != 0:
    out += CHARS[n % a]
    n //= a

print(out[::-1])