def dijkshtra(times, N, k):
    neighbours = {}
    weights = {}

    for i in range(len(times)):
        new_list = []
        neighbours.setdefault(times[i][0], []).append(times[i][1])
        for j in range(2):
            new_list.append(times[i][j])
        weights[times[i][2]] = new_list
    print(neighbours)
    weight_list = [v for v in weights.values()]
    weight_values = [k for k in weights.keys()]
    derived_dict = list(zip(weight_list, weight_values))
    print(list(derived_dict))
    
    for key,values in neighbours.items():
        if key == k:
            visited_array[k] = True
            distance_array[k] = min(0, distance_array[k])
        for i in range(len(values)):
            if derived_dict[k-1][0][0] == k and derived_dict[k-1][0][1] == values[i]:
                dist = derived_dict[k-1][1]
            distance_array[values[i]] = min(distance_array[values[i]], distance_array[k] + dist)
    
    print(distance_array)


N = 6
distance_array = [float("inf")] * N
visited_array = [False] * N
print(distance_array, visited_array)
times = [
    [1,2,9],
    [1,4,2],
    [2,5,13],
    [4,2,4],
    [4,5,6],
    [3,2,3],
    [5,3,7],
    [3,1,5]
]

dijkshtra(times, N, k=1)