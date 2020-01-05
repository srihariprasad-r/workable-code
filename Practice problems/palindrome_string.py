def isPalindrome(x):
    reversed = 0
    pop = 0
    if x == 0 :
        return 'true'
    elif x < 0:
        return 'false'
    elif x %10 == 0:
        return 'false'
    else:
        while(x > reversed):
            pop =  x % 10
            x = x/10               
            reversed = (reversed *10 ) + pop     

    print(x, reversed)

    if (reversed == x or x == reversed /10):        
        return 'true'
    else:         
        return 'false'
    
a = isPalindrome(-121)
print(a)