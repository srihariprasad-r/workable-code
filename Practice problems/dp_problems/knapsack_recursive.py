"""
from functools import wraps

def trace(func):
    separator = '|  '
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        trace.recursion_depth -= 1
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')
        return result
    return traced_func
"""

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
# result = trace(knapsack_recursive)
print(knapsack_recursive(wt, val, w, n))