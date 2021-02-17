"""
0

1 1

2 3 5

8 13 21 34
"""
def number_factorial_pattern(n):
    a, b, c = 0, 1, 0
    for i in range(n):
        for _ in range(i):
            print(a, end=" ")
            c = a + b
            a = b
            b = c
        print("\n")        
        
number_factorial_pattern(5)
