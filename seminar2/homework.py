# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n. 
# Обоснуйте выбор парадигм.
def multiplication_tables_one(n):
     for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end="\t")
        print()

def multiplication_table_two(n):
    for i in range(1, n+1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i*j}")
        print()

num = int(input('Enter a number: '))
multiplication_tables_one(num)
print()
multiplication_table_two(num)