n = int(input())

arr = [int(x) for x in input().split()]

print(' '.join(str(x) for x in sorted(arr, key=lambda x: x)))