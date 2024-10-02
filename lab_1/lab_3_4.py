from collections import Counter


def calculate_frequency(s):
    """Вычисляет частоту символов в строке."""
    if not s:
        return Counter()
    return Counter(s)


def most_common_frequency(frequencies):
    """Возвращает частоту самого распространенного символа в строках."""
    if not frequencies:
        return 0
    return max(frequencies.values())


def calculate_deviation(s, max_common_freq):
    """Вычисляет квадратичное отклонение частоты самого распространенного символа."""
    freq = calculate_frequency(s)
    common_freq = most_common_frequency(freq)
    return (common_freq - max_common_freq) ** 2


def sort_strings_by_deviation(strings):
    """Сортирует строки по квадратичному отклонению частоты самого распространенного символа."""
    all_frequencies = Counter()

    # Вычисляем частоты для всех строк и суммируем их
    for s in strings:
        all_frequencies += calculate_frequency(s)

    # Находим максимальную частоту самого распространенного символа
    max_common_freq = most_common_frequency(all_frequencies)

    # Сортируем строки по отклонению
    return sorted(strings, key=lambda s: calculate_deviation(s, max_common_freq))


# Пример использования
strings = [
    "apple",
    "banana",
    "kiwi",
    "orange",
    "strawberry",
    "plum"
]

sorted_strings = sort_strings_by_deviation(strings)

print("Sorted strings by quadratic deviation of the most common character frequency:")
for s in sorted_strings:
    print(s)
