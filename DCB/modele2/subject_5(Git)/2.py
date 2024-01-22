import datetime
import random

class User():
    name = ""
    surname = ""
    secondname = ""

    def __init__(self, name, surname, secondname):
        self.name = name
        self.surname = surname
        self.secondname = secondname

    def getFullName(self):
        return f" {self.secondname} {self.name} {self.surname}"

class Student(User):
    year_of_admission = random.randint(1995, 2024)

    def __init__(self, name, surname, secondname, year_of_admission):
        super().__init__(name, surname, secondname)
        self.year_of_admission = year_of_admission

    def getFullName(self):
        return "Студент " + super().getFullName() + " год поступления " + str(self.year_of_admission)

    def getCourse(self):
        cours = int(datetime.datetime.now().year) - self.year_of_admission
        if cours <= 4:
            return f'Он сейчас на {cours} й курс(е)'
        return 'Окончил обучение или еще не поступил'


class Teacher(User):
    name = ""
    surname = ""
    secondname = ""

    students = list()

    def __init__(self, name, surname, secondname):
        super().__init__(name, surname, secondname)

    def getFullName(self):
        return f'Учитель {super().getFullName()}'

    def removeStudent(self, index):
        self.students.pop(index)

    def getStudents(self):
        return self.students

    def addStudent(self, newName, newSurname, newSecondname, newYear):
        self.students.append([newName, newSurname, newSecondname, newYear])


Student1 = Student("Александр", "Владимирович", "Иванов", Student.year_of_admission)
print(Student1.getFullName())
print(Student1.getCourse())

Teacher1 = Teacher("Виолета", "Николавевна", " Петрова")
print(Teacher1.getFullName())

print('Добавили двух студентов в список к преподователю Петрова')
Teacher1.addStudent( "Юлия", "Валерьевна", "Токмагашева", random.randint(1,5))
Teacher1.addStudent("Анастасия", "Борисовна", "Пилецкая", random.randint(1,5))
print(Teacher1.getStudents())

print('Убрали из списка у преаодователя студента Пилецкая к преподователю')
Teacher1.removeStudent(1)

print('Проверили что данного студеента нет больше в списке')
print(Teacher1.getStudents())
