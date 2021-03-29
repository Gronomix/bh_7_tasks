"""
помидор может:
1. Расти (переходить на следующую стадию созревания)
2. Предоставлять информацию о своей зрелости

Атрибуты:
- **index** - номер
- **ripeness** - стадия зрелости (Отсутствует, Цветение, Зеленый, Красный)
- **states** - атрибут класса, в котором кортеж со стадиями зрелости (Отсутствует, Цветение, Зеленый, Красный)

Методы:
- инициализатор **\_\_init\_\_**, который принимает index и присваивает его self.index,
  а self.ripeness устанавливается первым значением из self.states
- метод **grow()**, который будет переводить томат на следующую стадию созревания
- метод **is_ripe()**, который будет проверять, что томат созрел (достиг последней стадии созревания).
  Должен возвращать True или False
"""

class Tomato:

    _index: int
    ripeness = (0, 1, 2, 3)
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

tomato = Tomato
print(tomato)
print(tomato._print_state)
tomato._print_state
