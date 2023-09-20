# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). 
# Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере 
# она значительно упростит вам жизнь.

import math 
def pirson(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y) 
    sum_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) 
    sum_sq_x = sum((xi - mean_x)**2 for xi in x)
    sum_sq_y = sum((yi - mean_y)**2 for yi in y) 
    return sum_xy / math.sqrt(sum_sq_x * sum_sq_y)


x = [1, 2, 3, 4, 5] 
y = [3, 6, 9, 12, 15] 
print("Корреляция Пирсона:", pirson(x, y))