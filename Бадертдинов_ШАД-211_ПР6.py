import numpy as np


def eigenvalues_eigenvectors(A):
    determinant = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    delta = (A[0, 0] + A[1, 1]) ** 2 - 4 * determinant
    if delta < 0:
        print('Матрица не имеет вещественных собственных значений')

    lambda1 = (A[0, 0] + A[1, 1] + np.sqrt(delta)) / 2
    lambda2 = (A[0, 0] + A[1, 1] - np.sqrt(delta)) / 2

    eigenvalues = np.array([lambda1, lambda2])
    eigenvectors = []

    for i in eigenvalues:
        if A[0, 1] != 0:
            x = 1
            y = -(A[0, 0] - i) / A[0, 1]
        else:
            if (A[0, 0] - i) != 0:
                x = 0
                y = 1
            else:
                x = 1
                y = 0

        eigenvector = np.array([x, y])
        eigenvectors.append(eigenvector)

    return eigenvalues, eigenvectors


A = np.array([[3, -2],
              [-4, 1]])
print('Нахождение собственных значений и собственных векторов методом непосредственного развертывания:')
print(eigenvalues_eigenvectors(A))
print('-------------------------------')


def power_iteration(A, max_iterations=10000, epsilon=1e-6):
    x = np.array([1.0, 1.0])
    lambda_prev = 0

    for i in range(max_iterations):
        if i % 3 == 0:
            x = x / np.linalg.norm(x)
        y = A @ x
        lambda_find = y[0] / x[0]

        delta_lambda = abs(lambda_find - lambda_prev)
        if delta_lambda < epsilon:
            return lambda_find, x
        lambda_prev = lambda_find
        x = y
    print('Метод не сошелся за:', max_iterations, 'итераций')


A = np.array([[3.0, -2.0],
              [-4.0, 1.0]])
print('Нахождение собственных значений и собственных векторов степенным методом:')
print(power_iteration(A))
