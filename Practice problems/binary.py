b = 50
c = 5
#print('{0:b}'.format(b))
#print('{0:b}'.format(c))
#print(b//2)
#print(b%2)

count = 0

def binary_conversion(n):
    d = bin(n)[2:]
    return d

def binary_validation(b,c):
    global count
    binary_b = binary_conversion(b)
    binary_c = binary_conversion(c)
    for i in range(0, (len(binary_b)-len(binary_c))+1):
        if binary_b[i:i+len(binary_c)] == binary_c:
            count += 1           
    return count


res = binary_validation(87,5)
print(res)