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
q = int(inputs[n][0])

min_city = 999999
out = -1
visited = [0] * (n + 1)
distance = [0] * (n + 1)
adj_dict = {}
girl_city_list = []

a = n + 1
for i in range(1, q+1):
    girl_city_list.append(int(inputs[a][0]))
    a += 1


def dfs(node, dist):
    visited[node] = 1
    distance[node] = dist
    if node in adj_dict:
        for k in adj_dict[node]:
            if not visited[k]:
                dfs(k, distance[node] + 1)
    return 

for i in range(1,n):
    adj_dict.setdefault(int(inputs[i][0]), []).append(int(inputs[i][2]))
    adj_dict.setdefault(int(inputs[i][2]), []).append(int(inputs[i][0]))

for i in range(1, n):
    if not visited[i]:
        dfs(i, 0)

for i in range(len(girl_city_list)):
    if distance[girl_city_list[i]] < min_city: 
        min_city = distance[girl_city_list[i]]
        out = girl_city_list[i]
    elif distance[girl_city_list[i]] == min_city and out < min_city:
        min_city = girl_city_list[i]
        out = girl_city_list[i]

print(out)