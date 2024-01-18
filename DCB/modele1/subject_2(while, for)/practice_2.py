#Задача 1
#Вариант 1
#для переменной i в диапозоне от 0 до 3(не включая 3) [0,1,2]:
#range(3) == [0,1,2]

for i in range(3):
    print('Итерация внешнего цикла : ', i)
    for j in range(2):
        print('Итерация внутреннего цикла : ', j)

#Вариант 2
a = int(input())
b = int(input())
#a,b = map(int,input("Введите кол-во итераций внешнего и внутреннего цикла через пробел").split(" "))
for i in range(a):
    print("Итерация внешнего цикла:",i)
    for j in range(b):
        print("Итерация внутреннего цикла цикла:",j)
"""
"""
#задача 2
#Вариант 1
n = int(input("Введите число: "))
#range(1, 10) == [1,2,3,4,5,6,7,8,9]
for i in range(1, 10):
    print(i, '*', n, '=', n * i)
#         3   *   5 =       5

#Вариант 2
a = int(input("Введите число: "))
print(f"1 * {a} =", a, f"2 * {a} =", 2*a, f"3 * {a} =", 3*a, f"4 * {a} =", 4*a, f"5 * {a} =", 5*a, f"6 * {a} =", 6*a, f"7 * {a} =", 7*a, f"8 * {a} =", 8*a, f"9 * {a} =", 9*a, f"10 * {a} =", 10*a)

#Вариант 3
a = int(input("Введите число"))
for i in range(1,10):
    print(i*a)
 
#Вариант 4
a = int(input())
for i in range(1, 10):
    print(i, "*", a, i*a)

#задача 3
#Вариант 1
for i in range(1, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i * j, end='\t')
    print()

#Вариант 2
i = 1
while i < 10:
    j = 1
    while j < 10:
        print("%4d" % (i * j), end="")
        j += 1
    i += 1
    print()
