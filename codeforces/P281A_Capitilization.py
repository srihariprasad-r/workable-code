cap_str = str(input())

mod_str = ""

if ord(cap_str[0]) >= 97 and ord(cap_str[0]) <= 122:
    mod_str += chr(ord(cap_str[0]) - 32)
    mod_str += cap_str[1:]

if len(mod_str) == 0:
    print(cap_str)
else:
    print(mod_str)