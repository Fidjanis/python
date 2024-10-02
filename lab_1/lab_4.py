def cyclic_shift_left(arr, positions=3):
    """Задача 1: Циклический сдвиг элементов массива влево на заданное количество позиций."""
    positions = positions % len(arr)  # Убедимся, что сдвиг не превышает длину массива
    return arr[positions:] + arr[:positions]


def elements_before_first_min(arr):
    """Задача 2: Найти элементы, расположенные перед первым минимальным."""
    if not arr:
        return []

    min_value = min(arr)
    min_index = arr.index(min_value)
    return arr[:min_index]


def is_local_maximum(arr, index):
    """Задача 3: Определить, является ли элемент по указанному индексу локальным максимумом."""
    if index <= 0 or index >= len(arr) - 1:
        return False  # Локальный максимум должен быть не на первом и не на последнем индексе

    return arr[index] > arr[index - 1] and arr[index] > arr[index + 1]


def elements_less_than_average(arr):
    """Задача 4: Найти все элементы, которые меньше среднего арифметического."""
    if not arr:
        return []

    average = sum(arr) / len(arr)
    return [x for x in arr if x < average]


def elements_more_than_three_times(arr):
    """Задача 5: Найти элементы, встречающиеся в исходном более трех раз."""
    from collections import Counter

    counts = Counter(arr)
    return [num for num, count in counts.items() if count > 3]


def main():
    while True:
        print("\nВыберите задачу:")
        print("1: Циклический сдвиг массива влево на 3 позиции")
        print("2: Элементы перед первым минимальным")
        print("3: Проверка локального максимума")
        print("4: Элементы меньше среднего арифметического")
        print("5: Элементы, встречающиеся более 3 раз")
        print("0: Выход")

        choice = input("Введите номер задачи (0-5): ")

        if choice == "0":
            break

        if choice == "1":
            arr = list(map(int, input("Введите целочисленный массив (через пробел): ").split()))
            result = cyclic_shift_left(arr)
            print("Результат:", result)

        elif choice == "2":
            arr = list(map(int, input("Введите целочисленный массив (через пробел): ").split()))
            result = elements_before_first_min(arr)
            print("Элементы перед первым минимальным:", result)

        elif choice == "3":
            arr = list(map(int, input("Введите целочисленный массив (через пробел): ").split()))
            index = int(input("Введите индекс для проверки локального максимума: "))
            result = is_local_maximum(arr, index)
            print("Является ли элемент локальным максимумом:", result)

        elif choice == "4":
            arr = list(map(int, input("Введите целочисленный массив (через пробел): ").split()))
            result = elements_less_than_average(arr)
            print("Элементы, меньше среднего арифметического:", result)

        elif choice == "5":
            arr = list(map(int, input("Введите целочисленный массив (через пробел): ").split()))
            result = elements_more_than_three_times(arr)
            print("Элементы, встречающиеся более 3 раз:", result)

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
