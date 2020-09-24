n = int(input())

coordinates = []
sum_coord = 0

while n > 0:
    coordinates.append([int(x) for x in input().split(" ")])
    n -= 1

for i in range(len(coordinates)):
    sum_coord += sum(coordinates[i])

if sum_coord == 0:
    print("YES")
else:
    print("NO")
