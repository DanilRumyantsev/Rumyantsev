# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().
#  удалить файл test.txt.

import os

print("Задание №1")
os.chdir("../PZ_11")

files = []

for obj in os.listdir():

    if os.path.isfile(obj):

        files.append(obj)

print(files)

print("Задание №2")

os.chdir("..")
os.mkdir("test")
os.mkdir("test/test1")

with open("./PZ_6/Практическая №6().pdf", "rb") as src_file:
    with open("test/Практическая №6().pdf", "wb") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ_6/PZ_6.py", "r", encoding="utf-8") as src_file:
    with open("test/pz6_ivahnenko.py", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ_6/PZ_6(2).py", "r", encoding="utf-8") as src_file:
    with open("test/pz6_ivahnenko.py", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ_6/PZ_6(3).py", "r", encoding="utf-8") as src_file:
    with open("test/pz6_ivahnenko.py", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ_7/PZ_7.py", "r", encoding="utf-8") as src_file:
    with open("test/test1/test.txt", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ_7/PZ_7(2).py", "r", encoding="utf-8") as src_file:
    with open("test/test1/test.txt", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

size = []
for file in os.listdir("test"):
    if os.path.isfile(os.path.join("test", file)):
        size.append(os.path.getsize(os.path.join("test", file)))

print(size)


print("Задание №3")

os.chdir("./PZ_11")

short_filename = ""
for filename in os.listdir():
    if len(filename) < len(short_filename) or short_filename == "":
        short_filename = filename

print(os.path.basename(short_filename))


print("Задание №4")
print("Файл из PZ_2 открыт")

pdf_folder = '../PZ_2'

pdf_filename = 'Практическое задание№2(2).pdf'

pdf_path = os.path.join(pdf_folder, pdf_filename)

if os.path.isfile(pdf_path):
    os.startfile(pdf_path)
else:
    print("Такого файла не существует")


print("Пункт №5")

os.chdir = '../test/test1'

file_path = os.path.join(os.chdir, 'test.txt')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('Файл успешно удален.')
else:
    print('Файл не найден.')