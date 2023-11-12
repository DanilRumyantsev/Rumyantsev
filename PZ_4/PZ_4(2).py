n = input("Введите целое число")
k = input("Введите второе целое число")
x = 0

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Условие не соблюдается")
        n = input("Введите целое число")

while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Условие не соблюдается")
        k = input("Введите целое число")

while n >= k:
    n -= k
    x += 1
y = n
print('Нацело: ', x)
print('Остаток: ', y)