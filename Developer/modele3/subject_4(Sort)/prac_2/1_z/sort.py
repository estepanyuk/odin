def sort(student_tuples):
    return sorted(student_tuples, key=str.lower)

student = ['john', 'A', 15]

print(sort(student))