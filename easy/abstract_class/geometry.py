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
    a: int
    b: int
    r: int

    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    @abstractmethod
    def get_perimeter(self):
        raise NotImplemented

    @abstractmethod
    def get_square(self):
        raise NotImplemented


class Circle(Shape):

    def __init__(self, a, b,  r):
        super().__init__(a, b, r)

    def get_perimeter(self, r):

        super().get_perimeter()
        perimeter = 2 * pi * r

        return perimeter

    def get_square(self, r):
        super().get_square()
        square = pi * r ** 2
        return square


class Rectangle(Shape):

    def __init__(self, a, b, r):
        super().__init__(a, b, r)

    def get_perimeter(self, a, b):
        super().get_perimeter()
        perimeter = (2 * a) + (2 * b)

        return perimeter

    def get_square(self, a, b):
        super().get_square()

        square = a * b
        return square


class Square(Rectangle):

    def __init__(self, a, b, r):
        super().__init__(a, b, r)

    def get_perimeter(self, a):
        super().get_perimeter()

        perimeter = 4 * a

        return perimeter

    def get_square(self, a):

        super().get_square()
        square = a ** 2
        return square


gp = Square(1, 2, 2)
print(gp)
Square()


