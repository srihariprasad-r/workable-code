def activitySelection(start, end):
    vect = {}
    ans = []

    for i in range(len(start)):
        vect.setdefault(i, []).append(start[i])
        vect.setdefault(i, []).append(end[i])

    sorted_dict = sorted(vect.items(), key=lambda e: e[1][1])

    cnt = 1
    prev = 0
    ans.append(sorted_dict[prev][1])

    for i in range(1, len(sorted_dict)):
        if sorted_dict[i][1][0] > sorted_dict[prev][1][0]:
            cnt += 1
            prev = i
            ans.append(sorted_dict[i][1])

    return cnt


start = [0, 1, 3, 5, 8, 5]
end = [6, 2, 4, 7, 9, 9]
print(activitySelection(start, end))