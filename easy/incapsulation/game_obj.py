"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    _x: int
    _y: int

    def __init__(self, x=4, y=6):
        self._x = x
        self._y = y

    @property
    def move(self):
        return self._x, self._y

    @move.setter
    def move(self, delta_x):
        self._x = delta_x

    @move.setter
    def move(self, delta_y):
        self._y = delta_y


gameobj = GameObject
print(gameobj.move)

