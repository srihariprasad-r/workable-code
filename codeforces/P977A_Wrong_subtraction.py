inp = [int(x) for x in input().split()]

n = inp[0]
k = inp[1]

while k > 0:
    last_digit = int(str(n)[-1])
    if  last_digit > 0:
        n -= 1
    elif last_digit == 0:
        n = n//10
    k -= 1

print(n)