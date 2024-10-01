from decimal import Decimal, getcontext

# Увеличиваем точность
getcontext().prec = 50

def solve_quadratic(a, b, c):
    # Проверка на ноль для 'a'
    if a == 0:
        if b == 0:
            if c == 0:
                return "Уравнение имеет бесконечно много решений."
            else:
                return "Уравнение не имеет решений."
        else:
            # Линейное уравнение bx + c = 0
            x = -c / b
            return [x]

    # Параметры уравнения
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)

    # Вычисление дискриминанта
    D = b**2 - 4 * a * c

    if D < 0:
        return "Уравнение не имеет действительных решений."
    elif D == 0:
        # Один корень (двойной корень)
        x = -b / (2 * a)
        return [x]
    else:
        # Два различных корня
        sqrt_D = D.sqrt()  # Вычисляем квадратный корень дискриминанта
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        return [x1, x2]

# Пример использования:
# Ввод коэффициентов a, b, c
a = input("Введите коэффициент a: ")
b = input("Введите коэффициент b: ")
c = input("Введите коэффициент c: ")

# Решение уравнения
solutions = solve_quadratic(a, b, c)

# Вывод решения
print("Решения уравнения:", solutions)
