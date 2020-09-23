arr = [int(x) for x in input().split()]
n = arr[0]
k = arr[1]

input_list = [0] + [int(x) for x in input().split()]

if input_list[k] == 0 and input_list.count('0') == len(input_list):
    print("0")
else:
    print(sum(1 if i > 0 else 0 for i in input_list[1:] if i >= input_list[k]))