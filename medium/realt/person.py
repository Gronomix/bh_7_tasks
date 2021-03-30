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

from medium.realt.house import House


class Human:

    name: str
    age: int
    _money: int
    _realty: set

    def __init__(
            self,
            name: str,
            age: int,
            _money: int = 0,
            _realty: set = None):
        if _realty is None:
            self._realty = set()
        else:
            self._realty = _realty

        self.name = name
        self.age = age

        self._money = _money


    def info(self):
        print(f' {self.name} {self.age} [{self._money}]:\n' + '\n'.join(self._realty))




    def earn_money(self, amount):
        self._money += amount
        print(f'Получено {amount} денег! Денег на счету: {self._money}')

    def decrease_cost(self, amount: int):

        if self._money < amount:
            raise ValueError

        else:
            self._money -= amount

    def make_deal(self, house: House):
        try:
            self.decrease_cost(house.cost)
        except ValueError as exc:
            print(f'Сделка не проведена {exc}')
        else:
            self._realty.add(house)








