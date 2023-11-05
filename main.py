# Завдання 3
# До вже реалізованого класу «Автомобіль» додайте необхідні перевантажені методи та оператори.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено")

    def car_info(self):
        print(f"Марка автомобіля: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}")

# Створення екземпляра класу
car_instance = Car("BMW", "X5", 2022)
car_instance.start_engine()
car_instance.car_info()
