arr = [int(x) for x in input().split()]

n = arr[0]
m = arr[1]

if n == 1 or m == 1:
    print("Akshat")
elif (n* m) %2 == 0:
    print("Malvika")
else:
    print("Akshat")