def printkeypadcombinations(str,ans):
    if len(str) == 0:
        print(ans)
        return
    
    ch = str[0]
    rest = str[1:]

    chr_from_dict = dict[int(ch)]

    for i in range(len(chr_from_dict)):
        printkeypadcombinations(rest, ans + chr_from_dict[i])
            

dict = {
    1 : 'abc',
    2 : 'def' ,
    3 : 'ghi',
    4 : 'jkl',
    5 : 'mnop',
    6 : 'qrst',
    7 : 'uv',
    8 : 'wxyz',
    9 : '.;' ,
    10 : '?!'
}
str = '573'
print(printkeypadcombinations(str, ""))