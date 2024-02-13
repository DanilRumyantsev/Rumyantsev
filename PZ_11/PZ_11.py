# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Элементы кратные 3:
# Произведение элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Элементы кратные 5:
# Количество элементов:
# Среднее арифметическое элементов:

f1_num = ['1 2 3 4 5 6 7 8 9 10']

f2_num = ['-1 -2 -3 -4 -5 -6 -7 -8 -9 -10']

f1 = open('text_file_1.txt', 'w', encoding='UTF-8')
f1.writelines(f1_num)
f1.close()

f1 = open('text_file_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f2 = open('text_file_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные')
f2.write('\n')
f2.writelines(f1_num)
f2.close()

f1 = open('text_file_1.txt')
proiz = 1
krat_3 = 0
for i in range(len(k)):
    if k[i] % 3 == 0:
        krat_3 += 1
for i in k:
    proiz *= i
min = k[0]
for elem in k:
    if elem < min:
        min = elem

f2 = open('text_file_2.txt', 'a', encoding='UTF-8')
f2.write("\n")
print('Количество элементов равных трём: ', krat_3, '\n','Произведение всех чисел: ', proiz, '\n', 'Минимальный элемент: ', min, file=f2)
f2.close()

f3 = open('text_file_3.txt', 'w', encoding='UTF-8')
f3.writelines(f2_num)
f3.close()

f3 = open('text_file_3.txt', encoding='UTF-8')
l = f3.read()
l = l.split()
for i in range(len(l)):
    l[i] = int(l[i])
f3.close()

f4 = open('text_file_4.txt', 'w', encoding='UTF-8')
f4.write('Исходные данные')
f4.write('\n')
f4.writelines(f2_num)
f4.close()

f3 = open('text_file_3.txt')
krat_5 = 0
for i in range(len(l)):
    if l[i] % 5 == 0:
        krat_5 += 1
sum = sum(l)
sr_znach = sum / len(l)

f4 = open('text_file_4.txt', 'a', encoding='UTF-8')
f4.write("\n")
print('Количество элементов', len(l), '\n','Количество элементов равных пяти: ', krat_5, '\n', 'Среднее арифмитическое: ', sr_znach, file=f4)
f4.close()