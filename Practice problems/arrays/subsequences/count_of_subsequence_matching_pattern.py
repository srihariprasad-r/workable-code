def subseq(s):
    if len(s) == 0:
        return ['']
    
    for i in range(len(s)):
        ch = s[i]
        left = s[0:i]
        right = s[i+1:]
        res = subseq(left+right)
        
        mres = []
        for i in range(len(res)):
            mres.append(res[i])
            mres.append(ch + res[i])
            
    return mres
            
            
def count_pattern_as_subsequence(s, ptn):
    subsequence_list = subseq(s)
    cnt = len([True for x in subsequence_list if str(x) == ptn])

    return cnt

s = 'ABCFGFPG'
pattern = 'GFG'
print(count_pattern_as_subsequence(s,pattern))