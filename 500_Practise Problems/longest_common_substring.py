"""
Given two strings 21 & s2, find longest common substring
Input:

s1= 'LCLC'
s2= 'CLCL'

output: 'CLC' 
"""

def longestcommonsubstring(s1, s2, k):
    l1, l2 = k, len(s2)
    match_list = [[0] * 4]* 4
    print(match_list)
    max = 0
    result = ""
    for i in range(l2):
        for j in range(l1):
            if s1[i] == s2[j]:
                if (i == 0 or j == 0):
                    match_list[i][j] = 1
                else:
                    match_list[i][j] = match_list[i - 1][j - 1] + 1
                print(result, max)
                if match_list[i][j] > max: 
                    result = ""
                    max = match_list[i][j]
                    result += s1[i+1-max:i+1]
                elif match_list[i][j] == max:
                    if result[:max+1].find(s1[i]) < 0:
                        result += s1[i- max+1:i+1]
            else:
                match_list[i][j] = 0
    return result
        


s1 = "LCLC"
s2 = "CLCL"
print(longestcommonsubstring(s1, s2, len(s1)))