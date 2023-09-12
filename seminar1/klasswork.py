#Максимум
def find_max_imperative(array:list) -> int:
    if len(array) > 0:
        max_num = array[0]
        for num in array:
            if num > max_num:
                max_num = num
        return max_num

def find_max_declarative(array:list) -> int:
    return max(array)

#Факториал
def calculate_factorial_declarative(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def calculate_factorial_imperative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Простое число
def check_prime_imperative(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def check_prime_declarative(number):
    get_list = [i for i in range(2, int(number ** 0.5) + 1)]
    if number < 2:
        return False
    list_is_bool = list(map(lambda x: number % x != 0, get_list))
    return all(list_is_bool)

#Реализовать функцию поиска элементов
def search_imperative(array, target):
    for num in array:
        if num == target:
            return True
    return False

def search_declarative(array, target):
    return target in array

#Реализовать функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел
def plus_minus_imperative(arr):
    pos_cnt, neg_cnt, zero_cnt = 0, 0, 0
    for el in arr:
        if el > 0: pos_cnt += 1
        elif el< 0: neg_cnt += 1
        else: zero_cnt += 1
    pos_frac = pos_cnt / len(arr)
    neg_frag = neg_cnt / len(arr)
    zero_frag = zero_cnt / len(arr)
    return pos_frac, neg_frag, zero_frag

def plus_minus_declarative(arr):
    pos_cnt = len(list(filter(lambda x: x > 0, arr)))
    neg_cnt = len(list(filter(lambda x: x < 0, arr)))
    zero_cnt = len(list(filter(lambda x: x == 0, arr)))
    counts = [pos_cnt, neg_cnt, zero_cnt]
    return list(map(lambda count: count / len(arr), counts))

