"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input:
ATTCGGGA

Output:
3
"""

def repetition(str):
    char= str[0]
    cnt = 0
    ans = 0
    for k in str:
        if k == char:
            cnt += 1
            ans = max(cnt, ans)
        else:
            char = k
            cnt = 1
    
    return ans

str = "ATTCGGGA"
print(repetition(str))