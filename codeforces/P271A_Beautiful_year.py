n = int(input())

for i in range(n + 1, n+1000):
    year_list = [j for j in str(i) if str(i).count(j) == 1]
    if len(year_list) == 4:
        print(i)
        break