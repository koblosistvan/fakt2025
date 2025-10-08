
"""
8 50
40
12
28
10
10
10
10
10

"""

inp = input().split()
N = int(inp[0])
K = int(inp[1])
T = [int(input()) for _ in range(N)]

start = 0
end = 0
t_sum = 0
best_start = -1
best_len = 100_001
for t in T:
    if t_sum < K:
        t_sum += t
        end += 1
    
    
    if t_sum == K:
        # print("!! ",start, end, t_sum, best_start, best_len)
        _len =  end-start
        if best_start == -1 or best_len > _len:
            best_start = start
            best_len = _len
        # t_sum -= T[start]
        # start += 1
        # end = max(start, end)

    while t_sum >= K:
        t_sum -= T[start]
        start += 1
        end = max(start, end)

print(best_len, best_start+1, sep='\n')
