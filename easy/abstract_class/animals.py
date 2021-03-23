"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"

"""

from abc import ABC, abstractmethod


class Animals(ABC):
    name: str
    a_type: str

    def __init__(self, name, a_type):
        self.name = name
        self.a_type = a_type

    @abstractmethod
    def says(self, name, a_type):
        return self


class Cat(Animals):

    def __init__(self, name, a_type):
        super(Cat, self).__init__(name, a_type)
        self.name = name
        self.a_type = a_type

    def says(self, name, a_type):
        print(f' {a_type} Кошка {name} говорит Мяу')


class Dog(Animals):

    def __init__(self, name, a_type):
        super(Dog, self).__init__(name, a_type)
        self.name = name
        self.a_type = a_type

    def says(self, name, a_type):
        print(f'{a_type} собака {name} говорит ГАВ')


class Cow(Animals):

    def __init__(self, name, a_type):
        super(Cow, self).__init__(name, a_type)
        self.name = name
        self.a_type = a_type

    def says(self, name, a_type):
        print(f' {a_type} Корова {name} говорит МУУУУ')


cow = Cow('Машка', 'Дикая')
cat = Cat('Шарик', 's')
dog = Dog('Феня', 'Домашняя')

print(cow.says('Машка', 'Дикая'))
print(dog.says('Шарик', 'Домашняя'))
print(cat.says('Феня', 'Домашняя'))



