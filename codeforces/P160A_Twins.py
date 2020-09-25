n = int(input())
coins = [int(x) for x in input().split()]

twin1_sum = 0
twin2_sum = sum(coins)
coin_count = 0

sorted_list = sorted(coins, key=lambda x: -x)

for i in range(len(sorted_list)):
    twin1_sum  += sorted_list[i]
    twin2_sum -= sorted_list[i]
    coin_count += 1

    if twin1_sum > twin2_sum:
        print(coin_count)
        break


