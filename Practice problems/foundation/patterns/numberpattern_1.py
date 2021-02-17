"""
1 

2 3

4 5 6 

7 8 9 10 

11 12 13 14 15
"""
def numberpattern(n):
    val = 1
    for i in range(1, n+1):
        for _ in range(i):
            print(val, end=" ")
            val += 1
        print("\n")        


numberpattern(5)