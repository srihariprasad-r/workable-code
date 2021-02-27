# top down
def f(n, cache):
    if cache[n] != -1:
        return cache[n]
    
    cache[n] = f(n-1, cache) + f(n-2, cache)

    return cache[n]
    
n = 3
cache = [-1] * (n+1)
cache[0] = 0
cache[1] = 1
print(f(n, cache))