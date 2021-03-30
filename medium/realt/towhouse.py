"""
Типовой дом

Методы:
- инициализатор **\_\_init\_\_**, который принимает адрес и начальную стоимость дома.
  self.area по умолчанию присваиваем 60
"""

from house import House


class Townhouse(House):
    def __init__(self, cost):
        super().__init__(cost)
        self.cost = 60
