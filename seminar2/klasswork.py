# четность числа
if __name__ == '__main__':
    num = int(input('Enter a number: \n'))
    if num % 2 ==0:
        print(True)
    else:
        print(False)

# print_numbers
def print_numbers(numbers):
    for num in numbers:
        print(num)

# quicksort
def quicksort(arr):
    if len(arr) <= 0:
        return arr
    else:
        base = arr[0]
        less = [x for x in arr[1:] if x <= base]
        greater = [x for x in arr[1:] if x > base]
        return quicksort(less) + [base] + quicksort(greater)

numbers = [8, 3, 1, 5, 9, 2, 7, 4, 6]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

# Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.
matrix = [[1,2,3], 
          [4,5,6],
          [7,8,9]]

trace = 0
for i, row in enumerate(matrix):
    for j, el in enumerate(row):
        if i == j:
            trace += el

print(trace)

# Добавить процедурную парадигму в имеющуюся реализацию вычисления следа.
def get_trace(matrix):
    trace = 0
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if i == j:
                trace += el
    return trace

matrix = [[1,2,3], 
          [4,5,6],
          [7,8,9]]
print(get_trace(matrix))

# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную систему счисления. 
# Обоснуйте сделанный выбор парадигм.
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

print(decimal_to_binary(25))