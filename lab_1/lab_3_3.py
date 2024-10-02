def average_ascii_weight(s):
    #"""Вычисляет средний вес ASCII-кода символов в строке."""
    if not s:
        return 0
    return sum(ord(char) for char in s) / len(s)

def max_triple_average_ascii_weight(s):
    #"""Вычисляет максимальный средний вес ASCII-кода троек подряд идущих символов."""
    if len(s) < 3:
        return 0
    max_average = 0
    for i in range(len(s) - 2):
        triple = s[i:i + 3]
        average = average_ascii_weight(triple)
        max_average = max(max_average, average)
    return max_average

def calculate_deviation(s):
    #"""Вычисляет квадратичное отклонение."""
    avg_weight = average_ascii_weight(s)
    max_triple_avg = max_triple_average_ascii_weight(s)
    return (avg_weight - max_triple_avg) ** 2

def sort_strings_by_deviation(strings):
    #"""Сортирует строки по квадратичному отклонению."""
    return sorted(strings, key=calculate_deviation)

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

print("Sorted strings by quadratic deviation:")
for s in sorted_strings:
    print(s)
