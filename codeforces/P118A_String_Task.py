str_input = str(input())

consonant = ""

vowels = ['a', 'e', 'i', 'o','u', 'y', 'A', 'E', 'I', 'O','U','Y']

for i in range(len(str_input)):
    if str_input[i] in vowels:
        continue
    else:
        consonant += '.'        
        if (ord(str_input[i]) >= 65 and ord(str_input[i]) <= 90): 
            consonant +=  chr(ord(str_input[i]) + 32)
        else:
            consonant +=  str_input[i]
        

print(consonant) 
