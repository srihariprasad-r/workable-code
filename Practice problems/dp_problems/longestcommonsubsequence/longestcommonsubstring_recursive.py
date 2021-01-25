def lcs(str1, str2, n, m, cnt):
    mx = 0
    if n == 0 or m == 0:
        return cnt
    lcs1 = cnt 
    if str1[n-1] == str2[m-1]:
        lcs1 =  lcs(str1, str2, n-1, m-1, cnt+1)
    lcs2 = lcs(str1, str2, n, m-1, 0)
    lcs3 = lcs(str1, str2, n-1, m, 0)
 
    return max(lcs1, max(lcs2, lcs3))
    
        

str1 = 'abcdebbbb'
str2 = 'abefg'
print(lcs(str1, str2, len(str1), len(str2), 0))