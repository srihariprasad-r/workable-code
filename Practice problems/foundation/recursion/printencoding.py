def printencoding(ques, ans):
    if len(ques) == 0:
        print(ans)
    
    if len(ques) == 1:
        if ques[0] == '0':
            return
        else:
            code = chr(ord('a') + int(ques[0]) - 1)   # encodes a-> 1, b-> 2...z-> 26
            print(ans + code)
    elif len(ques) > 1:
        ch = ques[0]            # recursion with first char eg: str = 123, recursion happens with 1/23
        ros = ques[1:]
        if ch == '0': 
            return
        else:
            code = chr(ord('a') + int(ch) - 1)
            printencoding(ros, ans + code)

        ch = ques[:2]       # recursion with first two chars eg: str = 123, recursion happens with 12/3
        ros = ques[2:]
        if int(ch) > 26:    # this check is to handle only till 26 chars
            return
        else:
            code = chr(ord('a') + int(ch) - 1)
            printencoding(ros, ans + code)                


str = '123'
printencoding(str, "")