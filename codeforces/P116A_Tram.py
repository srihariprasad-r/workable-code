n = int(input())

passengers = []

while n > 0:
    passengers.append([int(x) for x in input().split()])
    n -= 1

max_pass = 0
count = 0

for i in range(len(passengers)):
    for j in range(len(passengers[i])):
        if j == 1:            
            count += passengers[i][j]
        elif j == 0:
            count -= passengers[i][j]

        if max_pass < count:
            max_pass = count            

print(max_pass)            