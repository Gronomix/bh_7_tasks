"""
Куст с помидорами может:
1. Расти вместе с томатами
2. Предоставлять информацию о зрелости всех томатов
3. Предоставлять урожай

Атрибуты:
- **tomato_list** - список всех томатов

Методы:
- инициализатор **\_\_init\_\_**, который принимает args - произвольное количество томатов
  и сохраняет их в self.tomato_list
- метод **grow_all()**, который будет переводить все объекты из списка томатов на следующий этап созревания
- метод **all_are_ripe()**, который будет возвращать True, если все томаты из списка стали спелыми, False, если нет
- метод **give_away_all()**, который будет возвращать список томатов и очищать его на кусте томатов после сбора урожая
"""

from tomato import Tomato


class TomatoBush:

    def __init__(self, num):
        self.tomato_list = [Tomato(index) for index in range(0, num-1)]

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomato_list])

    def give_away_all(self):
        self.tomato_list = []


