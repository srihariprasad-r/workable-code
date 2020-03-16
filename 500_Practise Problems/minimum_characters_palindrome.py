"""
##ISSUE WITH CODE , NEED RETEST #####

Input - str = "ABC"

Output = 2

We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.
"""

def minCharpalindrome(str):
    delete_char = []
    i = 0
    j = len(str) - 1
    while(i <= j ):
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            delete_char.append(str[i])
            delete_char.append(str[j])
            i += 1
            j -= 1

    return len(delete_char)


str = "ABC"
cnt = minCharpalindrome(str)
print(cnt)
