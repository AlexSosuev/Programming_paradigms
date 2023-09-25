# Реализовать сортировку слиянием в любой парадигме. На вход ваша программа получает массив из
# чисел, а вернуть должна отсортированный массив.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]    
    left = merge_sort(left)
    right = merge_sort(right)    
    return merge(left, right)


def merge(left, right):
    arr_merg = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr_merg.append(left[i])
            i += 1
        else:
            arr_merg.append(right[j])
            j += 1
    
    while i < len(left):
        arr_merg.append(left[i])
        i += 1
    
    while j < len(right):
        arr_merg.append(right[j])
        j += 1
    
    return arr_merg

arr = [5, 2, 8, 4, 1, 9, 6, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# Написать программу в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, left, right, n):
    if left > right:
        return -1    
    mid = (left + right) // 2    
    if arr[mid] == n:
        return mid
    elif arr[mid] < n:
        return binary_search(arr, mid + 1, right, n)
    else:
        return binary_search(arr, left, mid - 1, n)


arr1 = [2, 4, 6, 8, 10, 12, 14]
n = 5
print(binary_search(arr1, 0, len(arr1)-1, n))

# Реализовать процедуру для вычисления MSE на любом языке в любой парадигме. Программа получает
# на вход два вектора и возвращает число - оценку MSE для этих векторов

def mse(arr1, arr2):
    if len(arr1) == len(arr2):
        return sum(map(lambda x, y: (x-y)**2, arr1, arr2))/len(arr1)
    else:
        return -1

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(mse(arr1, arr2))