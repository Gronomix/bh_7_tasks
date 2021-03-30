"""
Дом может:
1. Предоставлять информацию о себе
2. Изменять свою стоимость

Атрибуты:
- **address** - адрес дома
- **area** - площадь дома
- **cost** - стоимость дома

Методы:
- инициализатор **\_\_init\_\_**, который принимает адрес, площадь и начальную стоимость дома
- метод **increase_cost()**, который принимает значение, на которое нужно увеличить self.cost
- метод **decrease_cost()**, который принимает значение, на которое нужно уменьшить self.cost

"""


class House:

    address: str
    area: int
    cost: int

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def increase_cost(self, num):

        if num is not None:
            self.cost += num

            return self.cost

    def decrease_cost(self, num):

        if num is not None:
            self.cost -= num

            return self.cost

    def final_price(self):
        final_price = self.cost
        print(f'Final price: {final_price}')
        return final_price


house = House(35, 400)
house.increase_cost(20)
print(house.final_price())