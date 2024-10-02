from collections import Counter

# Частоты символов в английском алфавите (в процентах)
frequency_table = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
    'z': 0.07
}


def calculate_difference(string):
    # Привести строку к нижнему регистру и подсчитать частоты символов
    string = string.lower()
    counter = Counter(char for char in string if char.isalpha())

    if not counter:
        return float('inf')  # Если строка не содержит букв

    # Нахождение наиболее часто встречающегося символа
    most_common_char, most_common_freq = counter.most_common(1)[0]

    # Частота символа в алфавите
    alphabet_freq = frequency_table.get(most_common_char, 0)

    # Вычисление разницы
    difference = abs(most_common_freq - alphabet_freq)
    return difference


def sort_strings_by_difference(strings):
    return sorted(strings, key=calculate_difference)


# Пример использования
strings = [
    "Hello, world!", #1
    "Data science is fun.",
    "Python programming is interesting.",
    "I love coding."
]

sorted_strings = sort_strings_by_difference(strings)

print("Sorted strings by difference:")
for s in sorted_strings:
    print(s)
