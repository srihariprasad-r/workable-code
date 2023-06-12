"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""


def URLify(s, l):
    space = 0

    for i in range(len(s)):
        if s[i] == ' ': space += 1
    ls = list(s)

    needed = l
    
    for i in range(l-1, -1, -1):
        if s[i] == ' ':
            ls[needed-1] = '%20'
            needed -= 1
        else:
            ls[needed-1] = s[i]
            needed -= 1
            
    return ''.join(ls)
    
s = "Mr John Smith has"
l = 16
print(URLify(s, l))
