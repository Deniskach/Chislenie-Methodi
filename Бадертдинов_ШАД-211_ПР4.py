import numpy as np


def gauss_first(A, b):
    n = len(b)

    for i in range(n):
        factor = A[i, i]
        A[i, :] = A[i, :] / factor
        b[i] = b[i] / factor

        for k in range(i + 1, n):
            factor = A[k, i]
            A[k, :] = A[k, :] - factor * A[i, :]
            b[k] = b[k] - factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i+1:], x[i+1:])

    return f'x1={x[0]} \n x2={x[1]} \n x3={x[2]}'


A = np.array([[5, 0, 1],
              [2, 6, -2],
              [-3, 2, 10]])
b = np.array([11, 8, 6])
x = gauss_first(A, b)
print("Решение СЛАУ методом Гаусса:\n", x)
print('--------------------------------')


def gauss_pivot(A, b):
    n = len(A)
    for k in range(n - 1):
        max_row = np.argmax(np.abs(A[k:, k])) + k
        A[[k, max_row]] = A[[max_row, k]]
        b[[k, max_row]] = b[[max_row, k]]

        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, :] = A[i, :] - factor * A[k, :]
            b[i] = b[i] - factor * b[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return f'x1={x[0]} \n x2={x[1]} \n x3={x[2]}'


A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)
x = gauss_pivot(A, b)
print("Решение СЛАУ методом Гаусса с выбором ведущего элемента:\n", x)
print('--------------------------------')


def gauss_rectangle(A, b):
    n = len(b)

    for i in range(n - 1):
        for k in range(i + 1, n):
            for j in range(i + 1, n):
                A[k, j] = A[i, i] * A[k, j] - A[k, i] * A[i, j]
            b[k] = A[i, i] * b[k] - A[k, i] * b[i]

    x = np.zeros(n)
    if A[n-1, n-1] == 0:
      return None

    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n - 2, -1, -1):
        sum_ = 0
        for j in range(i+1, n):
            sum_ += A[i, j] * x[j]
        if A[i, i] == 0:
            return None
        x[i] = (b[i] - sum_) / A[i, i]

    return f'x1={x[0]} \n x2={x[1]} \n x3={x[2]}'


A = np.array([
    [2, 1, 4],
    [3, 2, 1],
    [1, 3, 3]])
b = np.array([16, 10, 16])
x = gauss_rectangle(np.copy(A), np.copy(b))
print("Решение СЛАУ методом Гаусса (Правило прямоугольника):\n", x)
print('\nНе смог реализовать метод LU-разложение')
