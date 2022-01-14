# method 1
def printpermutation(str, ans):
    if len(str) == 0:
        print(ans)
        return 
        
    for i in range(len(str)):
        ch = str[i]
        left = str[0:i]
        right = str[i+1:]
        mod_str = left + right

        printpermutation(mod_str, ans + ch)


str = 'abc'
print(printpermutation(str, ""))

# method 2
def recursion(s):
    def get_permutation(idx, ln, mp, lst, ans=''):
        if idx > ln:
            lst.append(ans)
            return

        for k, v in mp.items():
            if v > 0:
                mp[k] -= 1
                get_permutation(idx+1, ln, mp, lst, ans + k)
                mp[k] += 1

        return lst

    mp = {}

    for c in s:
        if c not in mp:
            mp[c] = 1
        else:
            mp[c] += 1

    return get_permutation(1, len(s), mp, [], '')


s = 'abc'
print(recursion(s))
