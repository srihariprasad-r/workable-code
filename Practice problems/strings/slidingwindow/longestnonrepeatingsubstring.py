s = {}

def longestnonrepeatingstring(str):
    i, j, mx, start, end = 0, 0, 0, 0, 0
    while j < len(str):
        if str[j] not in s:
            s[str[j]] = 1
        else:
            s[str[j]] += 1
        if len(s) == j - i + 1:
            mx = max(mx, j - i + 1)
            j += 1
        elif len(s) < j - i + 1:
            while len(s) != j - i +1:
                if str[i] in s and s[str[i]] > 0:
                        s[str[i]] -= 1
                if s[str[i]] == 0:
                    del s[str[i]]
                i += 1
            if not(mx > j - i + 1):
                start = i
                end = j
            j += 1
    return str[start: end+1]


str = 'pwwkew'
print(longestnonrepeatingstring(str))