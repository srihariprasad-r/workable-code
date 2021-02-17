"""
    *

    **

    ***

    ****

    *****
"""

def starpattern(n):
    for i in range(n):
        j  = 0
        while j <= i:
            print('*', end='')
            j += 1
        print('\n')

starpattern(5)