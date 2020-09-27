arr = [int(x) for x in input().split()]

n = arr[0]
m = arr[1]

min_stick = min(n,m)

if min_stick %2 != 0:
    print("Akshat")
else:
    print("Malvika") 