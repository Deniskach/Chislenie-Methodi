import math


def func(x):
    try:
        f = math.exp(x) / (math.exp(x) + 1) - 0.7
        return f
    except OverflowError:
        return None


def proiz(x):
    try:
        dif_f = math.exp(x) / (math.exp(x) + 1) ** 2
        return dif_f
    except OverflowError:
        return None


def func_newton_scaled(x0, c, tolerance=1e-10, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        f_x = func(x)
        if f_x is None:
            return None
        f_prime_x = proiz(x)

        if f_prime_x is None:
            return None

        if abs(f_prime_x) < 1e-12:
            return None

        delta_x = -c * f_x / f_prime_x
        x += delta_x

        if abs(f_x) < tolerance:
            return x

    return None


print('Метод Ньютона-Бройдена')
mas = [-2, -1, -0.5, 0, 0.5, 1, 2]
c_values = [0.3, 0.5, 0.7, 0.9]
for c in c_values:
    roots = set()
    for i in mas:
        root = func_newton_scaled(i, c)
        if root is not None:
            roots.add(round(root, 9))
        else:
            print('Не удалось найти корни')
    print(*roots)


"""---------------------------------------------"""


def func_secant(x, arr):
    res = 0
    for i in range(len(arr)):
        res += (x ** i) * arr[i]
    return res


def Secant(x0, x1, arr, tolerance=1e-10, max_iterations=100):
    for i in range(max_iterations):
        f_x0 = func_secant(x0, arr)
        f_x1 = func_secant(x1, arr)
        if abs(f_x1) < tolerance:
            return x1
        x_n = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_n
    raise ValueError("Достигнуто максимальное количество итераций. Корень не найден.")


print('\nМетод секущих')
arr = [6, -5, 1]
mas = [-10, -8, -4, -2, 2, 4, 8, 10]
mas_0 = len(mas) / 2
a = set()
for i in range(int(mas_0)):
    a.add(round(Secant(mas[i], mas[-i-1], arr), 2))
print(a)


"""---------------------------------------------"""


def func_iter(x, arr):
    res = 0
    for i in range(len(arr)):
        res += (x ** i) * arr[i]
    return res


def next_iter(x0, a=7):
    return 1/2 * (x0 + a/x0)


def Iteration(x0, tolerance=1e-10, max_iterations=100):
    for i in range(max_iterations):
        x_n = next_iter(x0)
        if abs(x_n - x0) < tolerance:
            return x_n
        x0 = x_n


print('\nМетод простых итераций')
print(Iteration(1))
