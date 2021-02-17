"""
                 *       

         *               *

*                                *

         *               *

                 *       
"""
def starpattern(n):
    os, st, ins = 2, 1, -1
    for i in range(n):
        for _ in range(os):
             print("\t", end=" ")
        for _ in range(st):
            print("*\t", end=" ")
        for _ in range(ins):
            print("\t", end=" ")
        if i >= 1 and i < n-1:
            print("*\t", end=" ")

        if i <= (n//2)-1:
            os -= 1
            ins += 2 
        else:
            os += 1
            ins -= 2

        print("\n")
starpattern(5)