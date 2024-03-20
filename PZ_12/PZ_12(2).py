# 2.Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
# 'Каир'].
vowels = 'аеёиоуыэюяaeiou'
words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

filtered_words = list(map(lambda word: ''.join(filter(lambda letter: letter.lower() not in vowels, word.upper())), words))
print(filtered_words)