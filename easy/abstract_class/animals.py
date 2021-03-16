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
    def says(cls, name,):
        cls.name = name




class Cat(Animals):

    print(f'Кошка {name} говорит Мяу')

class Dog(Animals):
        print(f'Собака {name} говорит ГАВ')

class Cow(Animals):
     print(f'Корова {name} говорит МУУУУ')



