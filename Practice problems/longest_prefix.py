def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    else:            
        prefix = strs[0]
        print(prefix)
        for i in range(1,len(strs)):
            print("in loop", strs[i])
            while (strs[i].find(prefix) == -1  or strs[i].find(prefix) > 0):
                prefix = prefix[:-1]
                print("after cut" , prefix)
        
    return prefix

#print("acc".find("c"))

list1 = ["c","acc","ccc"]
a = longestCommonPrefix(list1)
print(a)
        