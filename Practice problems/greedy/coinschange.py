def coinschange(coins, amount):
    cnt = 0
    ans = []

    # greedy approach: incorrect results when sum of two coins > next coin
    # failed ex: [1,3,5,6,9,11] amt = 15; ans will be 2 coins, but this provides 3 coins
    for i in range(len(coins)-1, -1, -1):
        while amount >= coins[i]:
            amount -= coins[i]
            cnt += 1
            ans.append(coins[i])

    return ans


# coins = [1,2,5,10,20,50,100,200,500,2000]
coins = [1, 3, 5, 6, 9, 11]
amount = 15
print(coinschange(coins, amount))
