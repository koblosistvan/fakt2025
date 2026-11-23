import sys
sys.stdin = open('_Megoldások\\Kódkupa\\26-1-MooDeng-input0.txt')

N = int(input().strip())
B = list(map(int, input().strip().split()))
S = list(map(int, input().strip().split()))

Jumps = -1

def back(steps, path):
    c = len(steps)
    if B[pos] > steps[-1]:       # ha még növelhető az utolsó lépésünk
        steps[-1] += 1
    else:                       # ha már nem növelhető az utolsó lépésünk
        steps = steps[:-1]
        path = path[:-1]
        back(steps, path)

steps = [1]
path = [0]
pos = 0
while True:
    # túlmennénk
    if pos + steps[-1] > N-1:
        back(steps, path)
        pos = path[-1]

    # találtunk egy utat, mentjuk
    elif pos + steps[-1] == N-1:
        print(steps)
        if (Jumps == -1) or (len(steps) < Jumps):
            Jumps = len(steps)
        back(steps, path)
        pos = path[-1]

    else: 
        # lépünk egyet
        pos += steps[-1]
        while S[pos] != -1:
            pos = S[pos]        # tovább csúszunk
        steps.append(1)
        path.append(pos)


print(Jumps)

sys.stdout.close()
