def calc(i, n):
    j = i * n
    j = j - 1
    if j % 2 == 0:
        print('Even!')
    else:
        print('odd!')
    return j

def f(n):
    for i in range(n):
        j = calc(i, n)
    return

if __name__ == '__main__':
    f(5)