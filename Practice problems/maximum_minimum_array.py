arr = [1000, 11, 445, 1, 330, 3000] 

def maximum_min_array(arr):
    max_element = arr[0]
    min_element = arr[0]
    mx = my = 0
    i = 0 
    while(i < len(arr)-1):
        if arr[i] < arr[i+1]:
            mx = max(max_element, arr[i+1])
            my = min(min_element, arr[i])
            max_element = mx
            min_element = my
        else:
            mx = max(max_element, arr[i])
            my = min(min_element, arr[i+1])
            max_element = mx
            min_element = my            
        i += 2
    
    print(mx,my)

maximum_min_array(arr)