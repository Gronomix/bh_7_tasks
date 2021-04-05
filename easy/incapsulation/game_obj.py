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

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y
        return self._x, self._y


gameobj = GameObject(5, 6)
gameobj.move(4, 5)

print(gameobj.move(5, 6))

