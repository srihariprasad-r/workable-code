from __future__ import print_function
import sys

def pattern_program(n):
    minimum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            #print(i,j)
            minimum = min(i,j)
            print (n - minimum+1, sep=' ', end= ' ')
        for j in range(n-1,0,-1):
            minimum = min(i,j)
            #print (n - minimum+1, sep=' ', end= ' ')
        
        print()

pattern_program(4)

print(sys.maxsize)