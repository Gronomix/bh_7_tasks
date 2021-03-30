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

    def __init__(self, address, area, cost):
        self.area = area
        self.cost = cost
        self.address = address

    def increase_cost(self, num: int):

        if num is not None:
            self.cost += num

            return self.cost

    def decrease_cost(self, num: int):

        if self.cost < num:
            self.cost = 0
        else:
            self.cost -= num



    #def final_cost(self) -> int:
        #cost = int(self.cost)
        #print(f'Финальная стоимость дома на {self.address}: {cost}')
        #return cost


house = House('Vashington str.', 35, 70)
house.increase_cost(20)
