a = [1,2, 3, 7, 6, 8, -1, -10, 15]

def unsorted_array(a):
    m = max(a)

    if m < 1:
        return 1

    if len(a) == 1:
        if a[0] == 1:
            return 2
        else:
            return 1
    
    new_list = [0] * m

    for i in range(len(a)):
        if a[i] > 0:
            if new_list[a[i] - 1] != 1:
                new_list[a[i] - 1] = 1
    
    for i in range(len(new_list)):
        if new_list[i] == 0:
            return i+1

#a= [1,3]
result = unsorted_array(a)
print(result)