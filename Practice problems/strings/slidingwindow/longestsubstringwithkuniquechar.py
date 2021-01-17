dct = {}
def longestsubstring(str,k):
    i, j, mx = 0, 0, 0
    while j < len(str):
        if str[j] not in dct:
            dct[str[j]] = 1
        else:
            dct[str[j]] += 1
        if len(dct) < k:
            j += 1
        elif len(dct) == k:
            mx = max(mx, j - i +1)
            j += 1
        else:
            if str[i] in dct:
                if dct[str[i]] == 0:
                    del dct[str[i]]
                else:
                    dct[str[i]] -= 1
            i += 1
            j += 1
    return mx # str[i:j+1]

str = 'aaaacccebebebe'
k = 3
print(longestsubstring(str,k))