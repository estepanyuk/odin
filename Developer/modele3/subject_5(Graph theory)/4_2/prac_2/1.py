class Person():
    def __init__(self, name, surname, secondname):
        self.name = name
        self.surname = surname
        self.secondname = secondname

    def getFullName(self):
        return self.name + ' ' + self.surname + ' ' + self.secondname

class Student(Person):
    def __init__(self, name, surname, secondname, year):
        super().__init__( name, surname, secondname)
        self.year = year

    def getCorse(self):
        return 'Студент сейчас на ' + str(self.year) + ' курсе'

class Teacher(Person):
    def __init__(self, name, surname, secondname, students):
        super().__init__(name, surname, secondname)
        self.students = students

    def addStudents(self, student):
        self.students.append(student)

    def removeStudents(self, index):
        self.students.pop(index)

    def getStudents(self):
        print(f'У учителя {self.getFullName()} учаться: ')
        for i in self.students:
            print(i.getFullName())


student1 = Student('Александр', 'Владимирович', 'Снупарьский', 3)
student2 = Student('Константин', 'Иванович', 'Муварьский', 4)
student3 = Student('Данила', 'Русланович', 'Костюков', 5)

teacher = Teacher('Степанюк', 'Екатерина', 'Геннадьевна', [student1])
print(student1.getFullName())
print(student1.getCorse())
print(student2.getFullName())
print(student2.getCorse())
print(student3.getFullName())
print(student3.getCorse())
print('-----------------------------------')
teacher.addStudents(student2)
teacher.addStudents(student3)
teacher.getStudents()
print('-----------------------------------')
teacher.removeStudents(2)
teacher.getStudents()








