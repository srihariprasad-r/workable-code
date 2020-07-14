"""
Given a string, get substring which is the longest with non repeating characters
"""


def longestnonrepeating(X):
    dict_str = {}
    start, st, maxLen = 0, 0, 0
    dict_str[X[0]] = 0    
    for i in range(1, len(X)):
        if X[i] not in dict_str.keys():
            dict_str[X[i]] = i
        else:
            if dict_str[X[i]] >= st:
                curLen = i - st
                if maxLen < curLen:
                    maxLen = curLen
                    start = st
                st = dict_str[X[i]] + 1
            dict_str[X[i]] = i
    
    return X[start:start+maxLen]

X = 'ABDEFGABEF'
print(longestnonrepeating(X))