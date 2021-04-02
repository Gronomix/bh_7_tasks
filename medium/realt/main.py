from house import House
from person import Human
from towhouse import Townhouse


if __name__ == '__main__':


    house = House('Vashington str.', 60, 70)
    house2 = House('Vashington str2.', 60, 70)
    house.increase_cost(30)
    townhouse = Townhouse('Gagarina str', 110)

    alexander = Human('Sasha', 27)
    alexander.info()
    alexander.earn_money(200)
    alexander.earn_money(200)
    alexander.make_deal(house)
    alexander.make_deal(townhouse)
    alexander.make_deal(house2)
    alexander.decrease_cost(20)



