'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())

sum_degrees = sum(list(map(int, input().split())))

if 2*(n-1) == sum_degrees:
    print("Yes")
else:
    print("No")