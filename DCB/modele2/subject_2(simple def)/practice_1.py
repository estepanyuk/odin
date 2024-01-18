#задача 1 Простейшие арифметические операции
'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
третий - операция, которая должна быть произведена над ними.
Если третий аргумент +, сложить их; если —, то вычесть;
* — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''

def arithmetic(agr1, agr2, op):
    if op == '/':
        return agr1 / agr2
    elif op == '+':
        return agr1 + agr2
    elif op == '-':
        return agr1 - agr2
    elif op == '*':
        return agr1 * agr2
    else:
        return 'Неизвестная операция'

a1 = int(input("Первое значение " ))
a2 = int(input("Второе значение " ))
op = input('Операции +, -, *, / ')

print(arithmetic(a1,a2,op))


#задача 2 Високосный год
"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""

def is_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

year = int(input('введите год: '))
print(is_year(year))

#задача 3 Времена года
"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
"""
def season(num):
    if num in (12, 1, 2):
        return 'Зима'
    elif num in (3, 4, 5):
        return 'Весна'
    elif num in (6, 7, 8):
        return 'Лето'
    elif num in (9, 10, 11):
        return 'Осень'
    else:
        return 'Неправильный номер'

month = int(input('Введите номер месяца: '))
print(season(month))

#задача 4 Квадрат
"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения 
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

def square(a):
    return(a*4,a*a,round((2**0.5*a),2))
print(square(a=int(input())))


from math import sqrt

def square(x):
    perimeter = x * 4
    area = x ** 2
    diagonal = round(x * sqrt(2), 2)

    return perimeter, area, diagonal

while True:
    c = square(int(input('Сторона x = ')))
    print(c[0], ' - Периметр', '\n', c[1], ' - Площадь', '\n', c[2], ' - Диагональ', '\n', sep = '')