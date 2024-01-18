def sort(student_tuples):
    return sorted(student_tuples, key=lambda student: student[1]) # сортируем по возрасту

student = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'C', 10),
    ]

print(sort(student))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age

student_objects = [
    Student('john', 'С', 10),
    Student('jane', 'B', 12),
    Student('dave', 'A', 15),
]

sort = sorted(student_objects, key=lambda student: student.age)  # сортируем по возрасту
print(sort)
