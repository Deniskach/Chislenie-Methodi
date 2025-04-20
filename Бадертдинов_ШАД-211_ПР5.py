import numpy as np


def simple_iteration(A, b, e=0.001):
    n = len(b)
    alpha = np.zeros((n, n))
    beta = np.zeros(n)
    A_copy = A.astype(float).copy()
    for i in range(n):
        beta[i] = b[i] / A_copy[i, i]
        alpha[i, :] = -A_copy[i, :] / A_copy[i, i]
        alpha[i, i] = 0

    x0 = beta
    x1 = np.dot(alpha, x0) + b
    while np.linalg.norm(x1 - x0) > e:
        x0 = x1
        x1 = np.dot(alpha, x0) + beta
    a = ''
    for i in range(n):
        a += f'x{i}={x1[i]}\n'
    return a


A = np.array([[10, 1, 1],
              [2, 10, 1],
              [2, 2, 10]
              ])
b = np.array([12, 13, 14])
print('Решение СЛАУ методом простых итераций:')
print(simple_iteration(A, b))
print('--------------------------------------')


def seidel(A, b, e=0.001, max_iter=1000):
    n = len(b)
    x = np.zeros(n)
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x) < e:
            return x_new
        x = x_new
    return x


A = np.array([[10, 1, 1],
              [2, 10, 1],
              [2, 2, 10]
              ])
b = np.array([12, 13, 14])
print('Решение СЛАУ методом Зейделя:')
print(*seidel(A, b))
