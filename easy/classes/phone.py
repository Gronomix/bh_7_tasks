"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:

    brand: str
    model: str
    year_of_issue: int

    def __init__(self, brand, model, year_of_issue):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue

    def receive_call(self, name):
        print(f'Звонит {name}')

    def get_info(self, brand, model, year_of_issue):
        a = (brand, model, year_of_issue)
        return print(a), print(self.brand + self.model + str(self.year_of_issue))

    def __str__(self):
        return f'Информация об устройстве:\n Бренд: {self.brand}\n Модель: {self.model}\n ' \
               f'Год выпуска: {self.year_of_issue}'


phone = Phone('Samsung', ' A_51 ', 2001)
print(phone.receive_call('Водитель Веры\n'))
print(phone.get_info('Samsung', ' A_51 ', 2001))
print(phone.__str__())


