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

    value: int
    num: int

    def __init__(self, value=0, num=1):
        self.value = value
        self.num = num

    def increase(self, num=1):

        if self.num is not None:
            self.value += num

            return self.value
        else:
            raise StopIteration

    def decrease(self, num=1):

        if self.num is not None:
            self.value -= num

            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        return self.value



count = Counter()

print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

print(count.decrease())
print(count.increase())
print(count.increase())
print(count.increase())
print(count.decrease())

