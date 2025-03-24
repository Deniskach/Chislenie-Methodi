def func(x, arr):
    res = 0
    for i in range(len(arr)):
        res += (x ** i) * arr[i]
    return res


def next(a, b, arr):
    try:
        s = a - func(a, arr) / (func(b, arr) - func(a, arr)) * (b - a)
        return s
    except ZeroDivisionError:
        return None


def method_hord(a, b, arr, max_iteartions=100, tolerance=1e-10):
    for i in range(max_iteartions):
        x_n = next(a, b, arr)
        if x_n is None:
            return None

        if abs(func(x_n, arr)) < tolerance:
            return x_n

        if func(a, arr) * func(x_n, arr) < 0:
            b = x_n
        else:
            a = x_n

    return None


arr = [6, -5, 1]
a_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
b = 10

s = set()
for i in a_values:
    k = method_hord(i, b, arr)
    if k is not None:
        s.add(round(k, 2))
print('Метод хордов: ', *s)


print('-------------------------------------------------')


