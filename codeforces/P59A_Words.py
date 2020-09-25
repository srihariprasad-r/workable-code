s = str(input())

upper_count = 0

for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        upper_count += 1

lower_count = len(s) - upper_count

if upper_count > lower_count:
    new_str = s.upper()
elif upper_count <= lower_count:
    new_str = s.lower()

print(new_str)