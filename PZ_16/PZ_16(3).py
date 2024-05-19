import pickle

class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_info(self):
        print(f"Брэнд: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")

def save_def(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_def(filename):
    with open(filename, "rb") as f:
        obj = pickle.load(f)
    return obj


computer1 = Computer("Apple", "M1", "16GB")
computer2 = Computer("Dell", "Intel i7", "32GB")
computer3 = Computer("HP", "AMD Ryzen 9", "64GB")

save_def(computer1, "computer1.pickle")
save_def(computer2, "computer2.pickle")
save_def(computer3, "computer3.pickle")

loaded_computer1 = load_def("computer1.pickle")
loaded_computer2 = load_def("computer2.pickle")
loaded_computer3 = load_def("computer3.pickle")

loaded_computer1.display_info()
loaded_computer2.display_info()
loaded_computer3.display_info()
