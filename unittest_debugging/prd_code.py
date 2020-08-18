def add_multiply(x, y):
    add = x + y
    multiple = multiply(x , y)
    return add , multiple


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError
    return x / y