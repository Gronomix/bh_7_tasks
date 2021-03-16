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

class Shape:
    a: int
    b: int
    r: int

    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r


    @abstractmethod
    def get_perimeter(self, a, b):
        perimeter = (2 * a) + (2 * b)
        return perimeter
    @abstractmethod
    def get_square(self, r):
        square = pi * r ** 2
        return square

class Circle(Shape):
    get_perimeter = (2 * a) + (2 * b)
    pass

class Rectangle(Shape):

    pass

class Square(Rectangle):
    pass

