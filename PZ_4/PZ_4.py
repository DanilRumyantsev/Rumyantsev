A , B = input("Введите число") , input("Введите второе число")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Не соблюдается условие!")
        A = input("Введите число")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Условие не соблюдается")
        B = input("Введите второе число")

C = 0

while A <= B:
    print(A)
    A += 1

