# Завдання 4
# До вже реалізованого класу «Книга» додайте необхідні перевантажені методи та оператори.


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def print_info(self):
        print(f"Назва книги: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

# Створення екземпляра класу
my_book_info = Book("Кобзар", "Т. Г. Шевченко", "вірші")
my_book_info.print_info()




