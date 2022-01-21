def recursion(idx, n, k, ans=[], res=[]):
    if idx > n or k < 0:
        return

    if k == 0:
        if ans not in res:
            res.append(ans)
        return

    for i in range(idx, n+1):
        recursion(idx, n,  k-i, ans + [i], res)
        for j in range(idx+1, n+1):
            recursion(idx+1, n, k-i-j, ans + [i] + [j], res)

    return res


n = 5
k = 7
print(recursion(1, n, k))