"""
* 

  *

    *

      *

        *

          *

            *
"""
def starpattern(n):
    st = 0
    for i in range(n+1):
        if i > 0:
            for _ in range(i):
                print(" ", end=" ")
        if i == st:
            print('*', end=" ")
        else:
            print(" ", end=" ")
        st += 1
        print("\n")
        

starpattern(6)