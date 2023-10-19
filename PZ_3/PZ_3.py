#Проверить условие "Число читается одинаково, слева на право и справа налево

def function(number): #Создаём функцию
    number_str = str(number) #Переводим числа в строку, чтобы потом её перевернуть

    return number_str == number_str[::-1] #возвращаем перевернутое число

your_number = input("Введите четырёхзначное число")

if function(your_number): #Создаем условие
    print(f"{your_number} - число читается одинаково")
else:
    print(f"{your_number} - число не читается одинаково")