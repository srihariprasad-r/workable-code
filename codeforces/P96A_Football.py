inp_str = str(input())

cnt = 0

if len(inp_str) < 7:
    print("NO")
else:
    i = 0
    while i <= len(inp_str) - 7:
        if ((inp_str[i:i+7].count('0')) == 7 or (inp_str[i:i+7].count('1')) == 7):
            cnt += 1
            print("YES")
            break
        i += 1

if cnt == 0 and len(inp_str) >= 7:
    print("NO")


