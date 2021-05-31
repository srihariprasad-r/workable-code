def firststring_subsequence_second(s1, s2):
    i = j = 0

    m = len(s1)
    n = len(s2)

    while j < m and i < n:
        if s1[j] == s2[i]:
            j += 1
        i += 1

    return j == m

s1 = 'AXY'
s2 = 'YDXCPA'
print(firststring_subsequence_second(s1,s2))