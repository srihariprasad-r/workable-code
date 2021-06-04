def string_circular_rotated(s1, s2):
    if s1 == 0:
        return
    
    for i in range(len(s1)):
        s1 = s1[1:] + s1[0]
        
        if s1 == s2:
            return True
    
    return False
    

s1 = 'ABCD'
s2 = 'DABC'
print(string_circular_rotated(s1, s2))