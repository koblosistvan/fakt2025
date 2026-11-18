def faktorialis(n): 
    if n == 0: return 1
    else: return n * faktorialis(n-1)
print(faktorialis(-2))