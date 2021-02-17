"""
        * 

      * * *

    * * * * *

      * * *

        *
"""
def starpattern(n):
    st, sp = 1, n//2
    for i in range(n):
        for _ in range(sp):
            print(" ", end=" ")
        for _ in range(st):
            print("*",end=" ")
        if i <= (n//2)-1:
            sp -= 1
            st += 2
        else:
            sp += 1
            st -= 2
        print("\n")
            

starpattern(5)