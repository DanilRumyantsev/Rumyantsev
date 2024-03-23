# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

odd_rows = filter(lambda x: x % 2 != 0, range(len(matrix)))

average_per_row = list(map(lambda i: sum(matrix[i]) / len(matrix[i]), odd_rows))

for i, avg in enumerate(average_per_row):
    print(f"Среднее арифметическое элементов строки {i * 2 + 1}: {avg}")