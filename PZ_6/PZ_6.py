import random
#Дан список ненулевых значений размера N. Проверить, образуют ли его элементы геометрическую прогрессию
#Если образуют, то вывести знаменатель прогрессии, если нет - 0

def function(a):
    if len(a) < 2:
        return False

    b = a[1] / a[0]

    for i in range(2, len(a)):
        if a[i] / a[i-1] != b:
            return 0
        else: return b

c = int(input("Введите размер массива"))

list = []

if c < 0:
    print("Введите положительное число")
else:
    t = 0

    while t < c:
        list.append(random.randint(0, 100))
        t += 1

list.sort()

print(list)

d = function(list)

if d:
    print(f"Элементы образуют прогрессию с знаменателем {d}")
else: print("Не образуют")