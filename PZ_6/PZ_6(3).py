import math
# Дано множество A из N точек (точки заданы своими координатами x, у). Найти пару
# различных точек этого множества с максимальным расстоянием между ними и само
# это расстояние (точки выводятся в том же порядке, в котором они перечислены при
# задании множества A).

def dist(a):
    n = len(a[0])
    max_dist = 0
    max_point = (0, 0)

    for i in range(n):
        for j in range(i +1, n):
            x1, y1 = a[0][i], a[1][i]
            x2, y2 = a[0][j], a[1][j]

            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            if dist > max_dist:
                max_dist = dist
                max_point = ((x1, y1), (x2, y2))

                return max_point, max_dist

a = [
    [1, 2, 3, 4], [5, 6, 7, 8]
]

res_point, res_dist = dist(a)
print(f"Максимальное расстояние: {res_dist}")
print(f"Пара точек: {res_point}")