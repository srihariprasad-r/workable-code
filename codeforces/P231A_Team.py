w = int(input())
cnt = 0

while(w > 0):
    problem = str(input())
    if problem.count('1') > 2:
        cnt += 1
    w -= 1

print(cnt)    