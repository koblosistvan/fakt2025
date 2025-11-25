import random
alap_szamok = []
for i in range(5):
   alap_szamok.append(random.randint(1,90))
print(alap_szamok)
en = input('Add meg a saját számaidat: ')
en2 = []
for i in range(5):
   en2.append(en[i].strip())
print(en2)