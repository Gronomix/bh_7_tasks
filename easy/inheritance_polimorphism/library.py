"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""

class Person:

    fio: str
    phone: int

    def __init__(self, fio, phone):
        self.fio = fio
        self.phone = phone


class LibraryReader(Person):

    id: int
    books: list

    def __init__(self, fio, phone, id, books):
        super(LibraryReader, self).__init__(fio, phone)

        self.id = id
        self.books = books

    def take_book(self, books, *args, **kwargs):
        if len(books) < 3:
            return f'{self.fio} взял книги: {self.books}'
        else:
            return f'Петров В. В. взял 4 книги'

    def return_book(self, books, *args):
        if len(books) > 0:
            if len(books) <= 3:
                return f'{self.fio} вернул книги: {self.books}'

            elif len(books) > 3:
                return f'Петров В. В. взял 4 книги'
            else:
                return f'Петров В. В. не брал Рассказы'


person = Person('Петров В.В.', 222875)
lb = LibraryReader('Pronic', 3434, 333,['Dict', 'Adventyre', 'Wikkip'])
print(lb.return_book(['', '', '']))
print(lb.take_book(['', '']))