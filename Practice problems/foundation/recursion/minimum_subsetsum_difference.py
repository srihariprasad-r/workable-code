import copy


def findminsubsetsum(arr):
    return abs(sum(arr[0]) - sum(arr[1]))


def recursion(idx, arr, k, n, res=[]):
    # print(idx, k)
    if idx == len(arr):
        el = all(map(lambda x: len(x) == n, k))
        if el:
            res.append(copy.deepcopy(k))
        return

    for i in range(len(k)):
        if len(k[i]) / 2 <= n:
            if len(k[i]) == 0:
                k[i].append(arr[idx])
                recursion(idx+1, arr, k, n, res)
                k[i].pop()
            else:
                k[i].append(arr[idx])
                recursion(idx+1, arr, k, n, res)
                k[i].pop()

    out = list(filter(lambda x: findminsubsetsum(x), res))
    return out


arr = [1, 2, 3, 4]
k = [[] for _ in range(2)]
print(recursion(0, arr, k, 2))
"""
[[[1, 2], [3, 4]], [[1, 3], [2, 4]], [[2, 4], [1, 3]], [[3, 4], [1, 2]]]
"""