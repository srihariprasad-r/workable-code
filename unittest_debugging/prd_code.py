def add_multiply(x, y):
    add = x + y
    multiple = multiply(x , y)
    return add , multiple


def add_multiply_subtract(x, y):
    add = x + y
    if x > y:
        multiple = multiply(x , y)
        return add, multiple
    else:
        difference = abs(subtract(x, y))
        return add , difference


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError
    return x / y