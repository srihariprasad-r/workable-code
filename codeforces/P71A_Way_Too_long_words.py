w = int(input())
 
while(w>0) :
    inp_str = str(input())
    new_str = inp_str[0]
    if len(inp_str) >= 11:
        new_str += str(len(inp_str[1:len(inp_str)-1]))
        new_str += inp_str[-1]
        print(new_str)
    else:
        print(inp_str)
    w -= 1