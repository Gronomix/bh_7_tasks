"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f' Выполняем {func.__name__}; args {args}; kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        return result
    return wrapper


def class_decorator(cls):
    functions = {name: func for name, func in cls.__dict__.items() if callable(func)}
    for name, func in functions.items():
        decorated = decorator(func)
        setattr(cls, name, decorated)
    return cls


class MetaClass(type):

    def __new__(msc, *args, **kwargs):
        new_cls = super.__new__(mcs, name, basses, attrs)
        functions = {name: name for name, func in new_cls.__dict__.items() if callable(func)}
        for name, func in functions.items():
            decorated = decorator(func)
            setattr(new_cls, name, decorated)
        return new_cls


class ASD(metaclass=MetaClass):

    at = 125

    def __init__(self):
        self.a = 1

    def some_func(self, some_arg=0):
        pass




asd = ASD()
asd.some_func(1)




