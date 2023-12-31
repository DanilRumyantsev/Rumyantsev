# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Найти количество слов, которые
# содержат ровно три буквы «А».

def three_A(s):
    words = s.split()
    count = 0

    for word in words:
        if word.count('А') == 3:
            count += 1

    return count

input_string = "АРХАНГЕЛЬСК АРБУЗ ЧАЙНАЯ АНАСТАСИЯ АРМАТУРА ОБРАЗ МАССА"
result = three_A(input_string.upper())
print(f"Количество слов с тремя буквами 'А': {result}")
