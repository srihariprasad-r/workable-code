"""
    * * * * * 

      * * * *

        * * *

          * *

            *
"""
def starpattern(n):
    st, sp = n, 0
    for _ in range(n):
        for _ in range(sp):
            print(" ", end=" ")
        for _ in range(st, 0, -1):
            print("*",end=" ")
        sp += 1
        st -= 1
        print("\n")
            

starpattern(5)