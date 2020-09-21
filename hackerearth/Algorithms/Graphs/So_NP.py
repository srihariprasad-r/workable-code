'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# import sys
# inputs = sys.stdin.read().splitlines()

arr = [int(x) for x in input().split()]

n = int(arr[0])
m = int(arr[1])
k = int(arr[2])

print(m)

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

for i in range(m):
    input_list = list(map(int,input().split()))    
    adj_dict.setdefault(int(input_list[0]), []).append(int(input_list[1]))
    adj_dict.setdefault(int(input_list[1]), []).append(int(input_list[0]))

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        connected_component += 1

if connected_component > k:
    print(-1)
else:
    print(m- n + k)        