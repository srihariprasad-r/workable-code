
def recursion(idx, n, k, ans=[], res=[]):
    if idx > n or k < 0:
        return

    if k == 0:
        if ans not in res:
            res.append(ans)
        return

    for i in range(idx, n+1):
        recursion(i, n,  k-i, ans + [i], res)
        for j in range(i+1, n+1):
            recursion(j+1, n, k-i-j, ans + [i] + [j], res)

    return res


n = 5
k = 7
print(recursion(1, n, k))