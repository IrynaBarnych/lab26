# Завдання 2
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
# До вже реалізованого класу «Стадіон» додайте необхідні перевантажені методи та оператори.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity, length, width):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
        self.length = float(length)  # Перетворення в числове значення
        self.width = float(width)
    def __sub__(self, other):
        return (self.capacity - other.capacity)

    def __mul__(self, other):
        square1 = self.length * self.width
        square2 = other.length * other.width
        return abs(square1 - square2)



stadion1 = Stadium("Олімпійський", "22.09.1923", "Україна", "Київ", 70050,
                   "150", "100")
stadion2 = Stadium("Донбас-Арена", "29.09.2009", "Україна", "Донецьк",  525180,
                   "105", "68")


difference = stadion1 - stadion2
print(f"Різниця в місткості стадіонів: {difference} осіб")

area_difference = stadion1 * stadion2
print(f"Різниця в площі стадіонів: {area_difference} квадратних метрів")
