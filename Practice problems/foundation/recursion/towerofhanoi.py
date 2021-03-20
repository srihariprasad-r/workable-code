def towerofhanoi(n, T1, T2, T3):
    if n == 0:
        return
    towerofhanoi(n-1 , T1, T3, T2)
    print(str(n) + " [" + T1 +  " -> " + T2 + "]")
    towerofhanoi(n-1, T3, T2, T1)


n = 3
towerofhanoi(n, 'A', 'B', 'C')