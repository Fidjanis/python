import numpy as np
import math


def erf(x, er=1e-8):
    sum_erf = 0
    term = x
    n = 0
    # while abs(term)>er:
    while True:
        old = sum_erf
        sum_erf += term
        if sum_erf == old:
            break
        n += 1
        term = (-1) ** n * (x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1))
        # print(term, old)

    return 2 / math.pi ** (1 / 2) * sum_erf


def gaussian_elimination(A, b):
    n = len(b)
    # прям ход гаусса
    for i in range(n):
        # подел стр на вед эл
        for j in range(i + 1, n):
            if A[j][i] != 0:
                factor = A[j][i] / A[i][i]
                A[j] = A[j] - factor * A[i]
                b[j] -= factor * b[i]

    # обрат ход (реш сист)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]

    return x


def calculate_residuals(A, b, x):
    # вычисл невяз
    residuals = b - np.dot(A, x)
    return residuals


# A = np.array([[1.00, 0.80, 0.64],
#               [1.00, 0.90, 0.81],
#               [1.00, 1.10, 1.21]], dtype=float)
# b = np.array([erf(0.80), erf(0.9), erf(1.10)], dtype=float)
#
# # решение сист
# x = gaussian_elimination(A.copy(), b.copy())
#
# # вычисл невяз
# residuals = calculate_residuals(A, b, x)
#
# print("Решение:", x)
# print("Невязки:", residuals)
# print("x1+x2+x3:", sum(x))
# print("erf(1):", erf(1.0))



A = np.array([[0.10, 0.20, 0.30],
              [0.40, 0.50, 0.60],
              [0.70, 0.80, 0.90]], dtype=float)
b = np.array([0.10, 0.30, 0.5], dtype=float)

x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Решение:", x)
print("Остаток (разность Ax-b):", A @ x - b)
print("Ранг матрцы A:", rank)
