def printdecreasingincreasing(n):
    if n == 0:
        return
    print(n)
    printdecreasingincreasing(n-1)
    print(n)

n = 5
print(printdecreasingincreasing(n))