def dijkshtra(times, N, k):
    neighbours = {}

    for i in range(len(times)):
        neighbours.setdefault(times[i][0], []).append(times[i][1])

    for key in neighbours.keys():
        if key == k:
            visited_array[k] = True
            distance_array[k] = min(0, distance_array[k])


def recursive_execution(neighbours, k):
   for key, val in neighbours.items():
        if key == k:
            visited_array[k] = True
            distance_array[k] = min(0, distance_array[k])
        for i in range(len(val)):
           if not(visited_array[val[i]]):
               dist = times[key][i][2]
               distance_array[key] = distance_array[key] + dist


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