def printsubsequence(str, ans):
    if len(str) == 0:
        print(ans)
        return 
        
    ch = str[0]
    rest = str[1:]

    printsubsequence(rest, ans + ch)
    printsubsequence(rest, ans + "")

str = 'abc'
print(printsubsequence(str, ""))