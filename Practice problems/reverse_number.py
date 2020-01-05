def reverse(a):
    rev = 0
    while(a != 0):
        rev = (rev*10) + (a%10)
        print(rev)
        a = a/10
        print(a)
        #print(rev, a)


#everse(37)

def even_odd_sum(n):
    sum_odd = 0
    sum_even = 0
    c = 1
    while(n != 0 ):
        #print("actual value: ", n)
        if (c%2 == 0):
            sum_even += n%10
        else:
            sum_odd += n%10
        #print("before :", n)
        n = n//10
        c += 1
        #print("after: ",n)
    print(sum_even, sum_odd)

even_odd_sum(124)