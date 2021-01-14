def lcs_recursive(x, y, n, m):
    if n== 0 or m == 0:
        return 0

    if x[n-1] == y[m-1]:
        return 1 + lcs_recursive(x, y, n-1, m-1)
    else:
        return max(lcs_recursive(x, y, n, m-1), lcs_recursive(x, y, n-1, m))

x = 'abcdegh'
y = 'abcdfr'
print(lcs_recursive(x,y, len(x), len(y)))