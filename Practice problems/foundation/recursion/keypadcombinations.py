def keypadcombinations(str):
    if len(str) == 0 :
        return ['']
    
    ch = str[0]
    rest = str[1:]
    
    res = keypadcombinations(rest)
    
    result = []
    
    chr_from_dict = dict[int(ch)]
    
    for i in range(len(chr_from_dict)):
        for j in range(len(res)):
            result.append(dict[int(ch)][i] + res[j])
            
    return result
            
    


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
    0 : '?!'
}
str = '0573'
print(keypadcombinations(str))