inp = [int(x) for x in input().split()]

first_banana = inp[0]
soldier_amt = inp[1]
banana_needed = inp[2]

total_amt = 0

while banana_needed > 0:
    total_amt += first_banana * banana_needed
    banana_needed -= 1


if total_amt <= soldier_amt :
    print("0")
else:
    print(total_amt - soldier_amt)