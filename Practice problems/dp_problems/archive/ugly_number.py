def ugly_number(n):
    ugly_number_2 = 2
    ugly_number_3 = 3
    ugly_number_5 = 5        

    index_2 = 0
    index_3 = 0
    index_5 = 0    

    arr = [0] * n

    arr[0] = 1

    for i in range(1,n):
        ugly_number = min(ugly_number_2, ugly_number_3, ugly_number_5)

        arr[i] = ugly_number
        
        if arr[i] == ugly_number_2:
            index_2 += 1
            ugly_number_2 = arr[index_2] * 2
        elif arr[i] == ugly_number_3:
            index_3 += 1
            ugly_number_3 = arr[index_3] * 3
        elif arr[i] == ugly_number_5:
            index_5 += 1
            ugly_number_5 = arr[index_5] * 5            

    print(arr)

ugly_number(150)


