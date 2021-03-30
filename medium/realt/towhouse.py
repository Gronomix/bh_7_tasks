"""
Типовой дом

Методы:
- инициализатор **\_\_init\_\_**, который принимает адрес и начальную стоимость дома.
  self.area по умолчанию присваиваем 60
"""

from medium.realt.house import House


class Townhouse(House):
    def __init__(self, address: str,  cost):
        super().__init__(address, 60, cost)

