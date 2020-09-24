inp_str = str(input())

valid_str = "hello"
concat_str = ""

pos_dict = {valid_str[i]: valid_str.count(valid_str[i]) for i in range(len(valid_str))}

for i in inp_str:
    if i in valid_str and (i in pos_dict):
        if pos_dict[i] > concat_str.count(i):
            concat_str += i

if concat_str == valid_str:
    print("YES")
else:
    print("NO")

