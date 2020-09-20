'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
inputs = sys.stdin.read().splitlines()

n = int(inputs[0][0])
m = int(inputs[0][2])
k = int(inputs[0][4])

connected_component=0
visited = [0] * (n+1)
adj_dict = {}

def dfs(node):
    visited[node] = 1
    if node in adj_dict:
        for k in adj_dict[node]:
            if not visited[k]:
                dfs(k)
    return 

for i in range(1, m+1):
    adj_dict.setdefault(int(inputs[i][0]), []).append(int(inputs[i][2]))
    adj_dict.setdefault(int(inputs[i][2]), []).append(int(inputs[i][0]))

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        connected_component += 1

print(m- n + connected_component)