import copy


def swap(s, i, j):
    s_i = s[i]
    s_j = s[j]

    left = s[0:i]
    middle = s[i+1:j]
    right = s[j+1:]

    return left + s_j + middle + s_i + right


def recursion(s, max, k):
    if int(s) > max:
        max = int(s)

    if k == 0:
        return max

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if int(s[j]) > int(s[i]):
                s = swap(s, i, j)
                max = recursion(s, max, k-1)
                s = swap(s, i, j)

    return max


s = '1234567'
print(recursion(s, int(s), 4))
