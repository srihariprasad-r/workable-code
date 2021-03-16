def recursion_basics(n):
    if n == 0:
        return
    recursion_basics(n-1)
    print(n)

n = 5
print(recursion_basics(n))