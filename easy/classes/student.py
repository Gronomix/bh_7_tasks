"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5

"""

class Student:
    surname: str
    name: str
    group: str
    average_score: int

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def print_student(self):
        print(str(self.surname) + str(self.name) + str(self.group) + str(self.average_score))

    def __gt__(self, other):
        if self.average_score >= other.average_score:

            return True
        else:
            return False

    def __repr__(self,):
        return f'Student {self.surname} {self.name} {self.group} {self.average_score}\n'



student1 = Student('Filips', 'Jhon', ' 1f', 6)
student2 = Student('Filip', 'Makc', ' 1f', 7)
student3 = Student('Filip', 'Valera', ' 1f', 9)
student4 = Student('Filip', 'Abdula', ' 1f', 5)
student5 = Student('Filip', 'Rahmet', ' 1f', 5)

some_student = [student1, student2, student3, student4, student5]
some_student.sort(reverse=True)
print(some_student)


