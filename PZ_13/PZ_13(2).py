# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import numpy as np

def sr_znach(c):
    return np.mean(c)

a = np.random.randint(1, 10, size=(5, 5))

print(f"Исходная матрица\n {a}")

b = a[::2]

print(f"Нечетные строки\n {b}")

means = np.apply_along_axis(sr_znach, axis=1, arr=b)

print(f"Среднее значение строк\n {means}")