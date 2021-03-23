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
    def says(self, name,):
        return self




class Cat(Animals):

    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.name = name

    def says(self, name):
        print(f'Кошка {name} говорит Мяу')

class Dog(Animals):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.name = name

    def says(self, name):
        print(f'Собака {name} говорит ГАВ')

class Cow(Animals):

    def __init__(self, name):
        super(Cow, self).__init__(name)
        self.name = name

    def says(self, name):
        print(f'Корова {name} говорит МУУУУ')


cow = Cow('')
cat = Cat('')
dog = Dog('')

print(cow.says('Машка'))
print(dog.says('Шарик'))
print(cat.says('Феня'))



