# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.
data_string = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'

def convert_to_dict(data_string):
    data_list = data_string.split()
    product_dict = {}

    for i in range(0, len(data_list), 6):
        product_name = data_list[i]
        sales = list(map(int, data_list[i+1:i+6]))
        product_dict[product_name] = sales

    return product_dict

def find_min_sales(products_dict):
    min_sales = {}

    for product, sales in products_dict.items():
        min_sales[product] = min(sales)

    return min_sales

data_dict = convert_to_dict(data_string)
min_sales_dict = find_min_sales(data_dict)

print("Минимальные продажи по каждому виду продукции:")
for product, min_sales in min_sales_dict.items():
    print(f"{product}: {min_sales} кг")