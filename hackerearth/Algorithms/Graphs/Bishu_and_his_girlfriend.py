'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
arr = [int(x) for x in input().split()]

n = arr[0]
m = arr[1] if len(arr) > 1 else 0

min_city = 999999
out = -1
visited = [0] * (n + 1)
distance = [0] * (n + 1)
adj_dict = {}
girl_city_list = []


def dfs(node, dist):
    visited[node] = 1
    distance[node] = dist
    if node in adj_dict:
        for k in adj_dict[node]:
            if not visited[k]:
                dfs(k, distance[node] + 1)
    return 

if m == 0: 
    m = n - 1

for i in range(m):
    input_list = list(map(int,input().split())) 
    adj_dict.setdefault(int(input_list[0]), []).append(int(input_list[1]))
    adj_dict.setdefault(int(input_list[1]), []).append(int(input_list[0]))

q = int(input())

for i in range(1, q+1):
    girl_city_list.append(int(input()))
    

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