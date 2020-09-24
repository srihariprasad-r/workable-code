n = int(input())
stones = str(input())

i = 0
j = 1
cnt = 0

while j < n:
    if stones[i] == stones[j]:
        cnt += 1    
    i += 1
    j += 1


if cnt > 0:
    print(cnt)
else:
    print("0")