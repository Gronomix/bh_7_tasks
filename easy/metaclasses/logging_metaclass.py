"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""

class MetaClass(type):

    def __new__(cls, *args, **kwargs):
        new_class = super.__new__(mcs, name, basses, attr)


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f' Выполняем {func.__name__}; args {args}; kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        return result
    return wrapper


def class_decor(cls):
    call_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}

    for name, func in call_attr.items():
        dec_func = decorator(func)
        setattr(cls, name, dec_func)
    return cls


@class_decor
class SomeClass:

    def __init__(self, name):
        self.name = name

    def some_method(self):
        print('hi')

    def some_method1(self):
        print(' Woy')

sc = SomeClass(1)