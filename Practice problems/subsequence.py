def subseq(s,t):
    t_p = 0
    s_p = 0 
    if len(s) == 0:
        return True
    while(t_p < len(t)):
        if (t[t_p] == s[s_p]):
            print(t[t_p], s[s_p])
            s_p += 1
            if (s_p == len(s)):
                return True
        t_p += 1
    return False    

s= "acb"
t = "ahbgdc"

d= subseq(s,t)
print(d)
