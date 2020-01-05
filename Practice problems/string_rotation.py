s = "qwertyu"
n= len(s)

def string_rotate(d):
    left_rotation = s[d:] + s[:d]
    right_rotation = s[n-d:] + s[:n-d]
    print(left_rotation, right_rotation)

string_rotate(2)