def generatesubsequence(str):

    if len(str) == 0:
        return ['']
    ch =  str[0]
    rest = str[1:]
    res = generatesubsequence(rest)

    result = []
    
    for i in range(len(res)):
        w_space = '' + res[i]
        wo_space = ch + res[i]
        result.append(w_space)
        result.append(wo_space)

    return result

str = 'abc'
print(generatesubsequence(str))