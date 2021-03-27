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