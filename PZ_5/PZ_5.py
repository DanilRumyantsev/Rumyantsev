#Составить функцию, которая выводит строку, содержащую задаваемое с клавиатуры число символов
def Myfunction():
    try:
        a = int(input("Введите число символов для строки"))
        if a < 0:
            raise ValueError("Введите положительное число")
        b = input("Введите символы, которые вы хотите повторить")

        if not b:
            raise ValueError("Поле пустое")

        c = b * a

        print(c)

    except ValueError:
        print("Некорректный ввод")

Myfunction()

