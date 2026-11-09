def eloallit(a, b, s):
    sa, sb = [], []
    i, j = 0, 0
    for k in range(len(s) - 1):
        if a >= s[k]:
            sa.append(0)
            sa[i] = s[k]
            i += 1
            a -= s[k]
        elif b >= s[k]:
            sb.append(0)
            sb[j] = s[k]
            j += 1
            b -= s[k]
    if a > 0 or b > 0:
        print("Hiba")
    else:
        print(sa, sb)
eloallit(4, 10, [5, 4, 3, 2, 1])