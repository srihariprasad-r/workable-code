n = str(input())
win = str(input())

A_win = win.count('A')
D_win = win.count('D')

if A_win > D_win:
    print("Anton")
elif A_win < D_win:
    print("Danik")
else:
    print("Friendship")