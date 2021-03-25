"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""

class BookCard:

    _author: str
    _title: str
    _publishing_house: str
    _year: int
    _num_pages: int
    _num_copies: int

    def __init__(self, _author, _title, _publishing_house, _year, _num_pages, _num_copies):
        self._author = _author
        self._title = _title
        self._publishing_house = _publishing_house
        self._year = _year
        self._num_pages = _num_pages
        self._num_copies = _num_copies

    def __gt__(self, other):
        if self._year > other.year:

            return True
        else:
            return False




    def __repr__(self,):
        return f'Книги отсортированы по году выпуска {self._year} "{self._author}, {self._title},{self._publishing_house}"'






book1 = BookCard('Shiller', 'Love is Deth', 'Монах Аристофан', 1981, 246, 4000)
book2 = BookCard('Pushkin', 'Письмо Няне', 'Mikki Maus Company', 1965, 24, 235)
book3 = BookCard('Александ Дюма', 'Три Мушкетера', 'Подвальная фабрика имени Ким ИР Сена', 1956, 567, 784)
book4 = BookCard('Жуль Верн', '20 000 лье под водой', 'Генеральный штаб подводной авиации', 1990, 543, 4)

book_list = [book1, book2, book3, book4]
book_list.sort()
print(book_list)

