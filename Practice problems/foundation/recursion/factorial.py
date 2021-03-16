def factorial(n):
    if n == 1:
        return 1
    fnm1 = factorial(n-1)
    fn = n * fnm1
    return fn

n = 5
print(factorial(n))