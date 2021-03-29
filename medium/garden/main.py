from Gardener import Gardener
from tomato_bush import TomatoBush
from tomato import Tomato


if __name__ == '__main__':

    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()