def reverse(x):
    if ord(str(x)[0]) == 45:
        #print(str(x)[::-1].split("-")[0])
        return str(x)[0] + str(x)[:-1:-1].split("-")[0]
    elif str(x)[-1] == '48':
        x = str(x)[:-1]
        print(x)
        return str(x)[:len(x):-1]
    else:
        return str(x)[::-1]

x = 1230
a = reverse(x)

print(a)

#print(ord('0'))