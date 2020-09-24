target = int(input())

steps = 0

while target > 0:
    if target % 5 >= 0:
        target -= 5
    elif target % 4 >= 0:
        target -= 4        
    elif target % 3 >= 0:
        target -= 3
    elif target % 2 >= 0:
        target -= 2                
    elif target % 1 >= 0:
        target -= 1
    steps += 1        

print(steps)
