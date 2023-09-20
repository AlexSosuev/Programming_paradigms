#Что за парадигма: конвертация
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celc = [0, 10, 20, 30]
temp_fahr = list(map(celsius_to_fahrenheit, temp_celc))
print(temp_fahr)

# Ответ: функциональная и процедурная парадигмы. Почему это так: создана функция для конвертации единиц 
# температуры и применена с помощью метода map, то есть она использована не только как процедура, но и как 
# функция функциональной парадигмы, с помощью map.


# Что за парадигма: стандартизация данных 
from math import sqrt
from statistics import mean, variance

def standardize(data):
    avg = mean(data)
    var = variance(data)
    std = sqrt(var)
    def stanardize_element(x):
        return (x - avg) / std
    return list(map(stanardize_element, data))

data = [1, 2, 3, 4, 5]
print(standardize(data))

# Ответ: функциональная, процедурная и структурная парадигмы. Почему это так: с одной стороны мы используем 
# функцию stanardize_element как отображение, но с другой -  объявляем внешнюю функцию standardize как обычную 
# процедуру внутри которой происходит последовательность шагов в рамках структурной парадигмы.

# Что за парадигма: reduce 
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)

# Ответ: это функциональная парадигма. Почему это так: суммирование чисел происходит без явного объявления цикла 
# и элементов на каждом шаге (это происходит под капотом метода reduce).

# Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет нормализацию 
# полученного массива по приведенной формуле нормализованного значения элемента, где 
#       ○ x_norm - нормализованное значение элемента 
#       ○ x - исходное значение элемента 
#       ○ x_max, x_min - максимальное и минимальное значение в массиве

def normalize(data):
    min_val = min(data)
    max_val = max(data)

    def normalize_element(x):
        return (x - min_val) / (max_val - min_val)
    return list(map(normalize_element, data))

# Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий число - количество 
# людей старше указанного возраста.

people = [
    {'name': 'Elizaveta', 'age': 25},
    {'name': 'Vasiliy', 'age': 30},
    {'name': 'Sergey', 'age': 35},
    {'name': 'Ivan', 'age': 40}
]

def filter_by_age(people:list, min_age:int) -> list:
    return list(filter(lambda pers: min_age <= pers['age'], people))

age = 30
filter_people = filter_by_age(people, age)
print(filter_people)
print(len(filter_people))

# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход подается массив, 
# где могут присутствовать дубликаты (а могут и не присутствовать). При применении к массиву, дубликаты должны быть 
# выведены на экран в виде списка.

def find_duplicates(numbers):
    unique_numbers = set()
    return list(filter(lambda x: x in unique_numbers or unique_numbers.add(x), numbers))

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 6]
duplicates = find_duplicates(numbers)