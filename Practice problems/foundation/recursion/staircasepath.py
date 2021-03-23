def staircasepath(n):
    # assumption is 3 steps can be taken [1,2,3] to reach destination
    if n == 0:
        return [""]
    elif n < 0:
        return []

    p1 = staircasepath(n-1) # this is for 1 step towards reach destination
    p2 = staircasepath(n-2) # this is for 2 steps towards reach destination
    p3 = staircasepath(n-3) # this is for 3 steps towards reach destination

    p = []

    for path in p1:
        p.append('1' + path)
    for path in p2:
        p.append('2' + path)
    for path in p3:
        p.append('3' + path)
    
    return p

n = 3
print(staircasepath(n))