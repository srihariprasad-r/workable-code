"""
    *****

    ****

    ***

    **

    *
"""

def starpattern(n):
    for i in range(n):
        j  = n - i
        while j > 0:
            print('*', end='')
            j -= 1
        print('\n')

starpattern(5)