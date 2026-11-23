W, S, D = map(int, input().split())

k = 0
s_remaining = 1
d_remaining = 7

while d_remaining > 0:
    size = W
    # beszáll hófehérke
    if s_remaining > 0:
        s_remaining -= 1
        size -= S

    # beszállnak a törpék
    d_fit_count = size // D
    d_remaining -= d_fit_count
    size -= d_fit_count * D

    # lemegyünk
    k += 1

print(k*2 - 1)
