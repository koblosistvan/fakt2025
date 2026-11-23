import sys
sys.stdin = open('_Megoldások\\Kódkupa\\26-1-2-LuckyDice-input0.txt')

N = int(input().strip())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

W1 = W2 = X = 0

for i in range(N):
    # első versenyző
    a = min(A[i], B[i])
    b = max(A[i], B[i])

    # második versenyző
    c = min(C[i], D[i])
    d = max(C[i], D[i])

    # dupla-e
    double_1 = True if a == b else False
    double_2 = True if c == d else False

    # dobás értéke
    value_1 = a*10 + b
    value_2 = c*10 + d

    if double_1 == double_2:
        # a pontszám dönt
        if value_1 == value_2:
            X += 1
        elif value_1 < value_2:
            W2 += 1
        else:
            W1 += 1
    else:
        # a dupla nyert
        if double_1:
            W1 += 1
        else:
            W2 += 1

print(W1, W2, X)
