import random

x1 = random.randint(1,8)

x2 = random.randint(1,8)

y1 = random.randint(1,8)

y2 = random.randint(1,8)

neit_poz = [x1, y1]

next_poz = [x2, y2]

print(x1, x2, y1, y2)

if neit_poz != next_poz:
    print("True")
else: print("False")