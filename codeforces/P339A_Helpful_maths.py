inp_str = str(input())

strlist = inp_str.split("+")
asc_str = sorted(strlist, key=lambda x: int(x))

print('+'.join(asc_str))
