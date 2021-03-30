"""
Садовник, который может:
1. Ухаживать за растением
2. Собирать с него урожай

Атрибуты:
- **name** - имя садовника
- **plants** - список с растениями, за которыми ухаживает садовник

Методы:
- инициализатор **\_\_init\_\_**, который принимает name - имя садовника
  и args - произвольное количество кустов томата
- метод **work()**, который заставляет садовника работать, что позволяет всем растениям расти
- метод **harvest()**, который проверяет, все ли плоды созрели.
  Если созрели все плоды - садовник собирает урожай (метод возвращает список всех томатов),
  если нет - метод печатает предупреждение, что томаты не созрели и возвращает None.

"""

class Gardener:

    name: str
    plant: list

    def __init__(self, name, plant, *args):
        self.name = name
        self._plant = plant


    def work(self):
        print('Садовник начал работу...')
        self._plant.grow_all()
        print('Садовник закончил работу')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Томаты еще не созрели! Ожидайте следующего лета')
