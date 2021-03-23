"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""
from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        raise NotImplemented

    @abstractmethod
    def get_square(self):
        raise NotImplemented


class Circle(Shape):

    r: int

    def __init__(self, r):

        self.r = r

    def get_perimeter(self, r):

        perimeter = 2 * pi * r

        return perimeter

    def get_square(self, r):

        square = pi * r ** 2
        return square


class Rectangle(Shape):

    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self, a, b):

        perimeter = (2 * a) + (2 * b)

        return perimeter

    def get_square(self, a, b):

        square = a * b
        return square


class Square(Rectangle):

    def __init__(self, a):
        super(Square, self).__init__(a)
        self.a = a

    def get_perimeter(self, a):

        perimeter = 4 * a

        return perimeter

    def get_square(self, a):

        square = a ** 2
        return square


gs = Circle
gs.get_perimeter(1, r=2)
print(gs.get_perimeter(1, r=2))
gr = Rectangle
gr.get_perimeter(1, 2, 3)
gr.get_square(1, 2, 3)
print(gr.get_perimeter(1, 2, 3), gr.get_square(1, 2, 3))
gsq = Square
print(gsq.get_square(1, 2))


