def sum_product(n,c):
    prod_even = 1
    sum_odd = 0

    while(n != 0 ):
        if (c%2 == 0):
            prod_even *= n%10
        else:
            sum_odd += n%10
        n = n//10
        c -= 1
    
    print(prod_even, sum_odd)
    
    if (prod_even % sum_odd == 0):
        return True
    else:
        return False

result = sum_product(2157,4)
#print(result)

print(2%5)
print(3%5)