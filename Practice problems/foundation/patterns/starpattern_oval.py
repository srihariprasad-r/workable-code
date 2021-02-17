"""
    * * *   * * * 

    * *       * *

    *           *


    *           *

    * *       * *

    * * *   * * *
"""
def starpattern(n):
    st, sp = (n/2) , 1
    for i in range(n+1):
        for _ in range(int(st)):
            print("*",end=" ")
        for _ in range(sp):
            print(" ", end=" ")
        for _ in range(int(st)):
            print("*",end=" ")
        if i < (n/2):
            sp += 2
            st -= 1
        else:
            st += 1
            sp -= 2
        print("\n")
            

starpattern(6)