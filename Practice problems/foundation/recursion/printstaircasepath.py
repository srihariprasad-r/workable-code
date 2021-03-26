def printstaircasepath(n, ans):
    if n == 0:
        print(ans)
        return
    elif n < 0:
        return

    printstaircasepath(n-1, ans + '1')
    printstaircasepath(n-2, ans + '2')
    printstaircasepath(n-3, ans + '3')

n = 4
print(printstaircasepath(n, ""))