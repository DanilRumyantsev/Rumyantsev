# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import random

matrix = [
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
]

odd_rows = filter(lambda x: x % 2 != 0, range(len(matrix)))

average_per_row = list(map(lambda i: sum(matrix[i]) / len(matrix[i]), odd_rows))

for i, avg in enumerate(average_per_row):
    print(f"Среднее арифметическое элементов строки {i * 2 + 1}: {avg}")