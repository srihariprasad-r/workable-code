import copy


def recursion(idx, s, n, tsets, k, res=[], map={}):
    if n == idx:
        k = [k[x] for x in range(len(k)) if len(k[x]) > 0]
        ans = list(set([sum(k[x]) for x in range(len(k))]))
        if len(k) > 1 and k not in res and len(ans) == 1 and ans[0] not in map:
            map[ans[0]] = k
            res.append(copy.deepcopy(k))
        return

    if idx > n - 1:
        return

    for i in range(len(k)):
        if len(k[i]) == 0:
            k[i].append(s[idx])
            recursion(idx+1, s, n, tsets + 1, k, res, map)
            k[i].pop()
        else:
            k[i].append(s[idx])
            recursion(idx+1, s, n, tsets, k, res, map)
            k[i].pop()

    return res


s = [2, 1, 4, 5, 6]
k = [[] for _ in range(len(s))]
print(recursion(0, s, len(s), 0, k))
"""
[[[2, 1, 6], [4, 5]], [[2, 4], [1, 5], [6]]]
"""
