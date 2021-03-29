"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s

from time import time, sleep


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'RUN {func.__name__}; args {args}; kwargs {kwargs}')
        start_time = time()
        print(f'{start_time}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        end_time = time() - start_time
        print(f'Время окончания {end_time}')
        print(f'Всего затрачено времени Х{end_time - start_time}')
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

sc = SomeClass(1)
sc.some_method()
