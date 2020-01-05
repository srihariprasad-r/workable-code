a = [1, 60, -10, 70, -80, 85] 

#sum = 0


def sum_close_to_zero(a):
    min = a[0]+a[1]
    sum = 0
    min_i = 0
    min_j = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sum = a[i] + a[j] 
            if abs(min) > abs(sum):
                min = sum
                min_i = i
                min_j = j

    print(min_i,min_j)

sum_close_to_zero(a)

                