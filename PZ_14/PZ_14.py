# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту). Посчитать
# количество полученных элементов.
import re
f1 = open('Dostoevskiy.txt', 'r', encoding='UTF-8')

text = f1.read()

sovp = re.findall(r'18\w+', text)

sovp_list = list(set(sovp))

print(sovp_list)