def fractionalKnapsack(profit, weight, capacity):
    res = 0
    arr = [0] * len(profit)

    for i in range(len(profit)):
        arr[i] = (profit[i], weight[i])

    # sort based on profit/weight ratio
    sorted_arr = sorted(arr, key=lambda e: -(e[0]/e[1]))

    for i in range(len(sorted_arr)):
        cur_profit = sorted_arr[i][0]
        cur_weight = sorted_arr[i][1]
        if capacity - cur_weight >= 0:
            capacity -= cur_weight
            res += cur_profit
        else:
            res += cur_profit * (capacity/cur_weight)
            break

    return res


profit = [9, 7, 25, 15, 12, 2, 8]
weight = [1, 2, 10, 3, 4, 1, 3]

print(fractionalKnapsack(profit, weight, 16))
