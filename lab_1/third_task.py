#Variant 6

#3. В порядке увеличения разницы между частотой наиболее часто встречаемого
# символа в строке и частотой его появления в алфавите

from collections import Counter

frequency_table = {
    'a': 8.17, "b": 1.49, 'c': 2.78, 'd': 4.25,
    "e": 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09,
    'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
    'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
    'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
    'y': 1.97, 'z': 0.07
}


def calculate_difference(string):
    string = string.lower()
    counter = Counter(char for char in string if char.isalpha())
    if not counter:
        return float('inf')

    most_common_char, most_common_freq = counter.most_common(1)[0]
    alphabet_freq = frequency_table.get(most_common_char, 0)
    difference = abs(most_common_freq - alphabet_freq)
    return difference


def sort_strings_by_difference(strings):
    return sorted(strings, key=calculate_difference)


#strings = [
    #"Hello, world!",
    #"Data science is fun.",
    #"Python programming is interesting?",
    #"I love coding."
    #"112313141",
    #"563473",
    #"51252764"
#]

#sorted_strings = sort_strings_by_difference(strings)
#print("Sorted string by difference:")
#for s in sorted_strings:
#print(s)

#6. Сортировка в порядке увеличения медианного значения выборки строк(прошлое
# медианное значение удаляется из выборки и производится поиск нового медианного значения)

import statistics


def calculate_median(strings):
    lengths = [len(s) for s in strings]
    if not lengths:
        return None
    return statistics.median(lengths)


def sort_string_by_median(strings):
    result = []
    while strings:
        median_length = calculate_median(strings)
        if median_length is None:
            break
        same_length_strings = [s for s in strings if len(s) == median_length]
        if same_length_strings:
            string_to_remove = same_length_strings[0]
    result.append(string_to_remove)
    strings.remove(string_to_remove)
    return result


strings = [
    "apple",
    "banana",
    "kiwi",
    "orange",
    "strawberry",
    "plum"
]

sorted_strings = sort_string_by_median(strings)
print("Sorted string by median length:")
for s in sorted_strings:
    print(s)


#8. Сортировка в порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и
#максимального среднего ASCII-кода тройки подряд идущих символов в строке

def average_ascii_weight(s):
    if not s:
        return 0
    return sum(ord(char) for char in s) / len(s)


def max_triple_average_ascii_weight(s):
    if len(s) < 3:
        return 0
    max_average = 0
    for i in range(len(s) - 2):
        triple = s[i:i + 3]
        average = average_ascii_weight(triple)
        max_average = max(max_average, average)
        return max_average


def calculate_deviation(s):
    avg_weight = average_ascii_weight(s)
    max_triple_avg = max_triple_average_ascii_weight(s)
    return (avg_weight - max_triple_avg) ** 2


def sort_strings_by_deviation(strings):
    return sorted(strings, key=calculate_deviation)


#strings = [
    #"apple",
    #"banana",
    #"kiwi",
    #"orange",
    #"strawberry",
    #"plum"
#]
#sorted_strings = sort_strings_by_deviation(strings)
#print("Sorted strings by quadratic deviation:")
#for s in sorted_strings:
    #print(s)


#12. Сортировка в порядке увеличения квадратичного отклонения частоты встречаемости самого распространённого
# символа в наборе строк от частоты его встречаемости в данной строке

def calculate_frequency(s):
    if not s:
        return Counter()
    return Counter(s)


def most_common_frequency(frequencies):
    if not frequencies:
        return 0
    return max(frequencies.values())


def calculate_deviation(s, max_common_freq):
    freq = calculate_frequency(s)
    common_freq = most_common_frequency(freq)
    return (common_freq - max_common_freq) ** 2


def sort_strings_by_deviation(strings):
    all_frequencies = Counter()
    for s in strings:
        all_frequencies += calculate_frequency(s)
        max_common_freq = most_common_frequency(all_frequencies)
        return sorted(strings, key=lambda s: calculate_deviation(s, max_common_freq))


#strings = [
    #"apple",
    #"banana",
    #"kiwi",
    #"orange",
   # "strawberry",
    #"plum"
#]

#sorted_strings = sort_strings_by_deviation(strings)

#print("Sorted string by quadratic deviation of the most common character frequency:")
#for s in sorted_strings:
    #print(s)
