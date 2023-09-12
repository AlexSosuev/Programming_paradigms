def quicksort_declarative(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_declarative(less) + [pivot] + quicksort_declarative(greater)


def quicksort_iterative(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


arr = [0, 3, -9, 15, -90, -15, -4, 5]

print(f"Итеративная сортировка: {quicksort_declarative(arr)}")
print(f"Декларативная сортировка: {quicksort_declarative(arr)}")