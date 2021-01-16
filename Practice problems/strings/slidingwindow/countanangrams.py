dct = {}
def countanagarams(str, ptr):
    k = len(ptr)
    for i in range(len(ptr)):
        if ptr[i] not in dct:
            dct[ptr[i]] = 1
        else:
            dct[ptr[i]] += 1

    count = len(dct)
    i, j, res = 0, 0, 0
    while j < len(str):
        if str[j] in dct:
            dct[str[j]] -= 1

        if str[j] in dct and dct[str[j]] == 0:
            count -= 1

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if count == 0:
                res += 1
            if str[i] in dct and dct[str[i]] == 0:
                dct[str[i]] += 1
                count += 1
            i += 1
            j += 1
    
    return res


str = 'aabaabaa'
ptr = 'abaa'
print(countanagarams(str, ptr))