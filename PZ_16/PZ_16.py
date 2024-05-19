# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".
class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Брэнд: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")


computer = Computer("Gigabyte", "Intel Core I5", "16 GB")
computer.display_info()