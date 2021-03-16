def power(x,n):
    if n == 0:
        return 1
    pnm1 = power(x,n-1)
    pn = x * pnm1
    return pn

x = 2
n = 5
print(power(x, n))