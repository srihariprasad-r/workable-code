arr = [int(x) for x in input().split()]

available_pairs = arr[0]
new_socks = arr[1]

runout_count = 0

for i in range(1, available_pairs + 1):    
    if new_socks * i <= available_pairs:
        available_pairs += 1

print(available_pairs)
