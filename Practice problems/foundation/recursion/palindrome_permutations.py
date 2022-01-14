def palindrome_partitions(s):
    def generate_partitions(idx, l, s, map, odd, lst=[]):
        if idx > l:
            res = ''
            res += s 
            if odd:
                res += odd
            rev = ''
            for i in range(len(s)-1, -1, -1):
                rev += s[i]
            
            res += rev
            lst.append(res)
            return

        for k, v in map.items():
            if v > 0:
                map[k] -= 1
                generate_partitions(idx+1, l, s + k, map, odd)
                map[k] += 1
        
        return lst

    map = {}

    for x in s:
        if x not in map:
            map[x] = 1
        else:
            map[x] += 1

    
    odd = 0
    ch_odd = ''
    new_len = 0

    for k, v in map.items():
        if v % 2 == 1:
            ch_odd = k
            odd += 1
        map[k] = v//2
        new_len += v//2

    lst = generate_partitions(1, new_len, '', map, ch_odd)

    return lst

s = 'ababc'
print(palindrome_partitions(s))  # ['abcba', 'bacab']
