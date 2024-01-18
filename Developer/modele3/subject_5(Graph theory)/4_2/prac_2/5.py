# class TriangleChecker:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def triagle(self):
#         if all(isinstance(side, (int, float)) for side in self.sides):
#             if all(side > 0 for side in self.sides):
#                 sort_sides = sorted(self.sides)
#                 if sort_sides[0] + sort_sides[1] > sort_sides[2]:
#                     return 'Ура, можно построить треугольник! '
#                 return 'Жаль, но не получиться сделать треугольник'
#             return 'Отрицальные числа вводить нельзя'
#         return 'Нужно вводить только числа'
#
#
# triagle1 = TriangleChecker([2, 3, 4])
# print(triagle1.triagle())
# triagle2 = TriangleChecker([10, 3, 4])
# print(triagle2.triagle())
# triagle3 = TriangleChecker(['2', 3, 4])
# print(triagle3.triagle())
# triagle4 = TriangleChecker([2, -3, 4])
# print(triagle4.triagle())


class Trianle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def checker(self):
        if not (isinstance(self.a, int) and isinstance(self.a, int) and isinstance(self.a, int)): print("нужно вводить только числа!")
        elif min(self.a, self.b, self.c) < 0: print("Из отрицательных чисел ничего не получится!")
        elif not(self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b): print("Нельзя составить треугольник")
        else: print("Вы создали Бермудский треугольник")

check1 = Trianle(3, 4, 5)
check2 = Trianle("a", 1, 2)
check3 = Trianle(-1, 1, 2)
check4 = Trianle(2, 2, 0)
check1.checker()
check2.checker()
check3.checker()
check4.checker()