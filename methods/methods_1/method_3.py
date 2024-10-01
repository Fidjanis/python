import numpy as np


def gaussian_elimination(A, b):
    n = len(b)
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поделить строку на ведущий элемент
        for j in range(i + 1, n):
            if A[j][i] != 0:
                factor = A[j][i] / A[i][i]
                A[j] = A[j] - factor * A[i]
                b[j] -= factor * b[i]

    # Обратный ход (решение системы)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]

    return x


def calculate_residuals(A, b, x):
    # Вычисление невязок
    residuals = b - np.dot(A, x)
    return residuals


# Пример системы уравнений
A = np.array([[2.34, -4.21, -11.61],
              [8.04, 5.22, 0.27],
              [3.92, -7.99, 8.37]], dtype=float)
b = np.array([14.41, -6.44, 55.56], dtype=float)

# Решение системы
x = gaussian_elimination(A.copy(), b.copy())

# Вычисление невязок
residuals = calculate_residuals(A, b, x)

print("Решение:", x)
print("Невязки:", residuals)
