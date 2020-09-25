n = int(input())
arr = [int(x) for x in input().split()]

start, end = 0, 0
max_count = 0

if n == 1:
    print("1")
else:
    for i in range(len(arr)-1):
        if arr[i + 1] >= arr[i]:
            end = i + 1       
        else:
            start = i + 1
            end = i + 1

        max_count = end - start + 1 if max_count < (end - start + 1) else max_count
    
    print(max_count)

        

