import time

start = time.time()
for _ in range(10**7):
    i = 5**10 / 2**20
end = time.time()

print(end - start)
