def knapsack_recursive(wt, val, w, n):
    if (n == 0 or w == 0):
        return 0

    if w >= wt[n-1]:
        return max(val[n-1] + knapsack_recursive(wt, val, w- wt[n-1], n-1),
                    knapsack_recursive(wt, val, w, n-1))
    
    if w < wt[n-1]:
        return knapsack_recursive(wt, val, w, n-1)

wt = [1, 2, 3, 5]
val = [1, 4, 7, 10]
w = 8
n = len(wt)
print(knapsack_recursive(wt, val, w, n))