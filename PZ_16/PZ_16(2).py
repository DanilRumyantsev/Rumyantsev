# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def display_info(self):
        print(f"{self.name} - мужчина, ему {self.age} год(а)/лет.")

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def display_info(self):
        print(f"{self.name} - девушка, ей {self.age} год(а)/лет.")


man = Man("Антон", 21)

woman = Woman("Нина", 23)

man.display_info()

woman.display_info()