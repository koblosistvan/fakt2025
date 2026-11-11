def eloallit(a,b,s):
    i=0
    j=0
    sa = []
    sb = []
    for k in range(len(s)):
        if a >= s[k]:
            sa.append(0)
            sa[i] = s[k]
            i = i+1
            a = a-s[k]
        elif b >= s[k]:
            sb.append(0)
            sb[j]= s[k]
            j = j+1
            b = b-s[k]
    if a > 0 or b > 0:
        return "Hiba!"
    else: 
        return sa, sb

print(eloallit(14,14,[7,6,5,4,3,2,1]))