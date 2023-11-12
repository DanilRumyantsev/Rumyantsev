#Даны координаты двух различных полей шахматной доски
#x1, y1, x2, y2(целые числа, лежащие в диопазоне 1-8).
#Проверить истинность высказывания: "Ладья за один ход
#может перейти с одного поля на другое"

x1 = input("Введите целое число от 1 до 8")

x2 = input("Введите целое число от 1 до 8")

y1 = input("Введите целое число от 1 до 8")

y2 = input("Введите целое число от 1 до 8")

print("neit_poz", x1, y1,"next_poz", x2, y2)

while type(x1) != int:
    try:
        x1 = int(x1)
    except ValueError:
        print("Ошибка")
        x1 = input("Введите целое число от 1 до 8")

while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print("Ошибка")
        x2 = input("Введите целое число от 1 до 8")

while type(y1) != int:
    try:
        y1 = int(y1)
    except ValueError:
        print("Ошибка")
        y1 = input("Введите целое число от 1 до 8")

while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print("Ошибка")
        y2 = input("Введите целое число от 1 до 8")


if x1 != x2 or y1 != y2:
    print("Ладья за один ход может совершить перейти на другое поле")
else:
    print("Ладья не может совершить ход")