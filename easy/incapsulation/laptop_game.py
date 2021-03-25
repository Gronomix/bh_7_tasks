"""
Написать класс Laptop (ноутбук), со следующими скрытыми атрибутами:

- cpu_cores - количество ядер процессора
- gpu_total - количество ГБ видеопамяти
- ram_total - количество ГБ ОЗУ

Определить методы:

- инициализатор __init__, с помощью которого присваиваются скрытые атрибуты
- метод can_play(game_name, cpu_cores, gpu_total, ram_total). Если требования игры
  меньше, чем характеристики компьютера, то вывести
  "На данном ПК есть возможность играть в {game_name}"
"""

class Laptop:

    _cpu_cores: int
    _gpu_total: int
    _ram_total: int

    def __init__(self, _cpu_cores, _gpu_total, _ram_total):
        self._cpu_cores = _cpu_cores
        self._gpu_total = _gpu_total
        self._ram_total = _ram_total

    def can_play(self, game_name):
        if self._cpu_cores >= 2:
            if self._gpu_total >= 4:
                if self._ram_total >= 8:
                    return f'На данном ПК есть возможность играть в {game_name}'
                else:
                    return f'Не жмись купи комп что бы играть в {game_name}'
            else:
                return f'Не жмись купи комп что бы играть в {game_name}'
        else:
            return f'Не жмись купи комп что бы играть в {game_name}'


laptop1 = Laptop(2, 4, 9)
laptop2 = Laptop(4, 8, 7)
print(laptop1.can_play('CuberPank'))
print(laptop2.can_play('CuberPank'))
