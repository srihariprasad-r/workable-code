import copy


def recursion(idx, arr, n, k, res=[]):
    if idx > len(arr) - 1:
        if n > 1:
            flag = True
            for i in range(len(k)):
                if not k[i] or len(k[i]) < 2:
                    flag = False
            if flag:
                res.append(copy.deepcopy(k))
            return

    for i in range(len(k)):
        if len(k[i]) == 0:
            k[i].append(arr[idx])
            recursion(idx+1, arr, n + 1, k, res)
            k[i].pop()
        else:
            k[i].append(arr[idx])
            recursion(idx+1, arr, n, k, res)
            k[i].pop()

    return res


arr = [6, 1, 2, 5]
k = [[], []]
o = recursion(0, arr, 1, k)
print(o)
