"""
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input:
5

Output:
4 2 5 3 1

"""

def permutation(n):
    if n == 1:
        return 1
    elif n==2 or n ==3:
        return 'NO SOLUTION'
    else:
        if (n%2 == 0):
            for i in range(2,n+1,2):
                print(i)
            for i in range(1,n,2):
                print(i)
        elif (n%2 != 0):
            for i in range(n-1,0,-2):
                print(i)
            for i in range(n,0,-2):
                print(i)

n = 5
print(permutation(n))
