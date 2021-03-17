"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:

    def __init__(self, value=0, num=1, start=None, end=None):
        self.value = value
        self.num = num
        self.start = start
        self.end = end

    def increase(self, num=1):

        if self.value < self.end:
            self.value += num
        else:
            raise StopIteration

    def decrease(self, num=1):

        if self.value > self.end:
            self.value -= num
        else:
            raise StopIteration

    def __iter__(self):
        if self.increase <= 0:
            return self.increase
        else:
            return self.decrease

    def __next__(self):
        return self



count = Counter(start=0, end= 30)
print(count)
mycount = iter(count)
