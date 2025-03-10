import numpy as np


# Метод половинного деления
arr = [6, -5, 1]
x = [2.5, 4]


def delitel(xn, arr):
    function = 0
    for i in range(len(arr)):
        function += arr[i] * (xn ** i)
    return function


def func_del(x, arr, tolerance=10 ** (-10)):
    x0, x1 = x[0], x[1]

    if delitel(x0, arr) * delitel(x1, arr) < 0:
        iterations = 0
        while abs(x1 - x0) > tolerance:
            x2 = (x0 + x1) / 2

            if delitel(x0, arr) * delitel(x2, arr) < 0:
                x1 = x2
            elif delitel(x2, arr) * delitel(x1, arr) < 0:
                x0 = x2
            iterations += 1
        return (x0 + x1) / 2


a = func_del(x, arr)
print('Метод половинного деления:', a)


# Метод Ньютона
def func(x, arr):
    res = 0
    for i in range(len(arr)):
        res += (x ** i) * arr[i]
    return res


def proiz(arr):
    pr = []
    for i in range(1, len(arr)):
        pr.append(arr[i] * i)
    return pr


def next(x0):
    return x0 - func(x0, arr) / func(x0, proiz(arr))


def func_newton(x, tolerance=10 ** (-10)):
    s = (next(x) - x) / (1 - ((next(x) - x) / (x - next(x))))
    while abs(s) > tolerance:
        s = (next(x) - x) / (1 - (next(x) - x) / (x - next(x)))
        x = next(x)
    return x


a = func_newton(8)
print('Метод Ньютона:', a)


# Упрощенный метод Ньютона
def deriv(arr):
    b = []
    for i in range(1, len(arr)):
        b.append(arr[i] * i)
    return b


def func_simple(x, arr):
    res = 0
    for i in range(len(arr)):
        res += (x ** i) * arr[i]
    return res


def proiz_simple(arr):
    pr = []
    for i in range(1, len(arr)):
        pr.append(arr[i] * i)
    return pr


def next_simple(x, x0):
    return x - func_simple(x, arr) / func_simple(x0, deriv(arr))


def func_newton_simple(x, tolerance=10 ** (-10)):
    s = (next(x) - x) / (1 - ((next(x) - x) / (x - next(x))))
    while abs(s) > tolerance:
        s = (next(x) - x) / (1 - (next(x) - x) / (x - next(x)))
        x = next_simple(x, x0)
    return x


x0 = 8
a = func_newton_simple(x0)
print('Упрощенный метод Ньютона:', a)

