"""
            * 

          * *

        * * *

      * * * *

    * * * * *
"""
def starpattern(n):
    sp, st = n - 1, 1
    for i in range(n):
        for _ in range(sp, 0, -1):
            print(" ", end=" ")
        for _ in range(st):
            print("*",end=" ")
        sp -= 1
        st += 1
        print("\n")
            

starpattern(5)