'''t = [5, 2,6, 8, 3, 6]


def hanyparos(t):
	db = 0
	for i in range():
		if t[i] % 2 == 0:
			db += 1
	return db

hanyparos (t)



fuggveny osszegzes (A[1...n])
    B := 0;
    Ciklus i= 1től n-ig
        Ha A[i] > 0;
            B := B+i
    Ciklus vége
    visszaad B
fuggveny vege



def osszegzes(a):
    b = 0
    for i in range(len(a)):
        if a[i] > 0:
            b += a[i]
    return b


SA  4, 1
SB  5, 2, 3, 1


def eloallit (a,b,s):
    i,j = 1, 1
    sa, sb = [],[]

    for k in range(len(s)):
        if a >= s[k]:
            sa.append(a)
            sa[i] = s[k]
            i += 1
            a = a - s[k]
        else:
            if b >= s[k]:
                sb.append(b)
                sb[j] = s[k]
                j += 1
                b = b -s[k]
    if a > 0 or b > 0:
        print('hiba')
    else: 
        print(sa)
        print(sb)

eloallit(14, 14, [7,6,5,4,3,2,1]) 



def lepcso(n):
    if n == 1:
        return 1
    else:
        return n + lepcso(n-1)

print(lepcso(3))
'''

def fakt(t):
 if t==1:return 1
 else:return t*fakt(t-1)
print(fakt(6))