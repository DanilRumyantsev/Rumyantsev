# 1. В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
import random

matrix = [
    [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
    [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)],
    [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]
]

negative = list(filter(lambda x: x < 0, [element for row in matrix for element in row]))

print(f"Элементы массива: {negative} Размер полученного массива: {len(negative)}")