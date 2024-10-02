import statistics

def calculate_median(strings):
    #"""Функция для вычисления медианной длины строк."""
    lengths = [len(s) for s in strings]
    if not lengths:
        return None
    return statistics.median(lengths)

def sort_strings_by_median(strings):
    #Функция для сортировки строк в порядке увеличения медианы их длины."""
    result = []

    while strings:
        # Вычисляем медиану
        median_length = calculate_median(strings)
        if median_length is None:
            break

        # Сортируем строки по длине (все, что равны медиане)
        same_length_strings = [s for s in strings if len(s) == median_length]

        # Добавляем все строки равные медиане в результат
        result.extend(same_length_strings)

        # Удаляем строки, которые были добавлены
        for s in same_length_strings:
            strings.remove(s)

    return result

# Пример использования
strings = [
    "apple",
    "banana",
    "kiwi",
    "orange",
    "strawberry",
    "plum"
]

sorted_strings = sort_strings_by_median(strings)

print("Sorted strings by median length:")
for s in sorted_strings:
    print(s)
