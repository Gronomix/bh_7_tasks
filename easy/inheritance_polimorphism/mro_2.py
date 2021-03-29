"""
Описать класс Device. Реализовать метод process_doc, который будет генерировать
raise NotImplementedError

Описать класс Scanner, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier
Реализовать метод process_doc, который будет печатать "Сканирую, отправляю факс: {name}"

Создать объект класса MFU. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Device:

    def process_doc(self):
        raise NotImplementedError


class Scanner(Device):

    name: str

    def __init__(self, name):
        self.name = name

    def process_doc(self, name):
        print(f'Сканирую документ: {self.name}')


class Copier(Device):
    name: str

    def __init__(self, name):

        self.name = name

    def process_doc(self, name):
        super().process_doc()
        print(f'делаю копию: {self.name}')


class MFU(Scanner, Copier):
    
    def __init__(self, name):
        super(MFU, self).__init__(name)
    
    def process_doc(self, name):
        super().process_doc()
        print(f'Сканирую, отправляю факс: {self.name}')


mfu = MFU
mfu.process_doc()


