def edit_distance(str1, st2, m , n):

    if m == 0:
        return n
    
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    else:
        return 1 + min(edit_distance(str1, str2, m, n-1),
                edit_distance(str1, str2, m-1, n),
                edit_distance(str1, str2, m-1, n-1)
        )



str1 = "saturday"
str2 = "sunday"
m = len(str1)
n = len(str2)

print(edit_distance(str1, str2, m-1 , n-1))
