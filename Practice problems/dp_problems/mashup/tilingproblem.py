def tilingproblem(n):
    cache = [0] * (n+1)
    
    cache[0] = 1
    cache[1] = 0
    
    for i in range(2, n+1):
        cache[i] = 2 * cache[i-2]
    
    return cache
    
n = 5
print(tilingproblem(n))