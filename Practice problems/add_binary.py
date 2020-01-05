def addBinary(a,b):
    i = len(a) - 1
    j = len(b) - 1
    sum = 0
    s_list = []
    carry = 0
    new_list = []
    while(i >= 0 or j >= 0):
        sum = carry
        print(sum)
        if i >= 0: sum += int(a[i]) - 0
        if j >= 0: sum += int(b[j])- 0
        print("new_sum:", sum)
        s_list.append(sum % 2)
        carry = sum /2
        print(carry)
        i -= 1
        j -= 1
        print(s_list)
    if carry > 0 : s_list.append(carry)
    new_list = ''.join(str(e) for e in s_list[::-1])
    #new_list = [str(s_list[x]) for x in range(len(s_list)-1,0,-1)]
    return new_list

a = "11"
b = "1"
c = addBinary(a,b)
print(c)
