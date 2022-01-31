def palindrome_permutations(s, tgt):
    def solution(idx, s, n, odd, map, tgt, ans='', res=[]):
        if idx >= n:
            rslt = ''
            rslt += ans
            if odd:
                rslt += odd

            rslt += ans[::-1]
            rs = [rslt[i:]+rslt[:i] for i in range(len(rslt))]
            if tgt in rs:
                res.append(rs[0])

            return

        for k, v in map.items():
            if v > 0:
                map[k] -= 1
                solution(idx+1, s, n, odd, map, tgt, ans+k, res)
                map[k] += 1

        return res

    map = {}
    for i in range(len(s)):
        if s[i] not in map:
            map[s[i]] = 1
        else:
            map[s[i]] += 1

    ch_odd = ''
    new_len = 0

    for k, v in map.items():
        if v % 2 == 1:
            ch_odd = k
        map[k] = v//2
        new_len += v//2

    return solution(0, s, new_len, ch_odd, map, tgt)


s = 'ABCCBA'
tgt = 'BAABCC'
print(palindrome_permutations(s, tgt))
# ['ABCCBA', 'CBAABC']
