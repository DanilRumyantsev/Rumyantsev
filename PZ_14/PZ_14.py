# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.
import re
f1 = open('Dostoevskiy.txt', 'r', encoding='UTF-8')

text = f1.read()

years = re.findall(r'\b\w*?\W*(\d{4})\W*\w*?\b', text)

matches = re.findall(r'\b\w*год\w*\b', text)

for year, match in zip(years, matches):
    print(f"{year} - {match}")