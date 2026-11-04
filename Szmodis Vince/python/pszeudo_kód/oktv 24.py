i=0
j=0
a=14
b=14
s=[7, 6, 5, 4, 3, 2, 1]
sa=[]
sb=[]


for k in range(len(s)):
    if a >= s[k]:
        sa.append(0)
        sa[k]=s[i]
        i+=1
        a=a-s[k]
    elif b>=s[k]:
        sb.append(s[k])
        j+=1
        b=b-s[k]

if a>0 or b>0:
    print('Hiba')
else:
    print(sa,sb)
