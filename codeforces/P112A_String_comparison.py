str1 = str(input())
str2 = str(input())

new_str1 = str1.lower()
new_str2 = str2.lower()

i = 0

cnt1 = 0
cnt2 = 0

while(i < len(str1)):
    if ord(new_str1[i]) < ord(new_str2[i]):
        print("-1")
        cnt1 += 1
        break
    elif ord(new_str1[i]) > ord(new_str2[i]):
        print("1")
        cnt2 += 1
        break
    else:
        i = i + 1

if cnt1 == 0 and cnt2 == 0:
    print("0")


