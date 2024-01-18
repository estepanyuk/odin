class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return repr((self.name, self.grade, self.age))

student_objects = Student('jane', 'B', 12)
print(student_objects)

# sort = sorted(student_objects, key=lambda s: s.age)
# print(sort)