"""
          * 

        *   

      *     

    *       

  *
"""
def starpattern(n):
    sp, st = n -1, 1
    for _ in range(n):
        for _ in range(sp, -1, -1):
            print(" ", end=" ")
        for _ in range(st):
            print("*", end=" ")
        if sp < n - 1:
            for _ in range(n-1-sp):
                print(" ", end=" ")
        print("\n")
        sp -= 1
        
starpattern(5)
