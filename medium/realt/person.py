"""
Человек может:
1. Предоставить информацию о себе
2. Заработать деньги
3. Купить дом

Атрибуты:
- **name** - имя
- **age** - возраст
- **money** - количество денег
- **realty** - недвижимость (список домов)

Методы:
- инициализатор **\_\_init\_\_**, который принимает name и age, присваивает их
  self.name и self.age соответственно. self.cash присваивает 0, а self.realty присваивает пустой список
- метод **info()**, который будет выводить поля name, age, realty и money.
- метод **earn_money()**, который принимает значение, на которое нужно увеличить money
- метод **make_deal()**, который принимает объект класса House или Townhouse,
  и если у человека достаточно денег, то списывает их с money и добавляет объект дома к self.realty

"""
from house import House


class Human:

    name: str
    age: int
    _money: int
    _realty: list

    def __init__(self):

        self.name = 'Victor'
        self.age = 30

        self._money = 0
        self._realty = []

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self._money}')
        print(f'House: {self._realty}')



    def earn_money(self, amount):
        self._money += amount
        print(f'Получено {amount} денег! Денег на счету: {self._money}')


    def _make_deal(self):

        cost = House.final_cost
        if self._money > cost:
            self._money -= cost
            self._realty.append(House.address)
            return print(f'Дом {House.address} приобретен {self.name}')
        else:
            return print('не достаточно дене')


human = Human()
human.earn_money(90)
human.earn_money(90)
human.earn_money(250)
human._make_deal
print(human._make_deal())



