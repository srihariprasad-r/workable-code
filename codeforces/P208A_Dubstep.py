inp_str = str(input())

inp_list = inp_str.split("WUB")

print(' '.join(str(x) for x in inp_list if len(x) > 0))