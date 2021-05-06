def lexicalorder(n):
    for i in range(1, 10):
        dfs(i, n)

def dfs(x, n):
    if x > n: return 
    print(x)
    for j in range(10):
        dfs(10*x+j, n)


n = 100
lexicalorder(n)