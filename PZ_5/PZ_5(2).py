def RectPS(x1, y1, x2, y2):
    P = 2 * (abs(x1 - x2) + abs(y1 - y2))
    S = abs(x1 - x2) * abs(y1 - y2)
    return P, S

x1 = float(input("Введите координату x"))
y1 = float(input("Введите координату y"))
x2 = float(input("Введите координату x2"))
y2 = float(input("Введите координату y2"))

per, ar = RectPS(x1 ,y1, x2, y2)
print(per, ar)