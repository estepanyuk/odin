#задача 1 Простейшие арифметические операции
'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
третий - операция, которая должна быть произведена над ними.
Если третий аргумент +, сложить их; если —, то вычесть;
* — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''
'''

def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return 'Неизвестная операция'

a1 = int(input('Введите первое значение: '))
a2 = int(input('Введите второе значение: '))
o = input('Операция +, -, *, /: ')

print(arithmetic(a1, a2, o))
'''

#задача 2 Високосный год
"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""
"""
def is_year(year):

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

year = int(input('введите год: '))
print(is_year(year))
"""

#задача 3 Времена года
"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
"""
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
"""
#задача 4 Квадрат
"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения 
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""
"""
from math import sqrt

def square(x):
    perimeter = x * 4
    area = x ** 2
    diagonal = round(x * sqrt(2), 2)

    return perimeter, area, diagonal

while True:
    c = square(int(input('Сторона x = ')))
    print(c[0], ' - Периметр', '\n', c[1], ' - Площадь', '\n', c[2], ' - Диагональ', '\n', sep = '')

"""
# задача 5 Банковский вклад
"""
Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. 
Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
"""
def bank(a, years):

    for year in range(years):
        a *= 1.1
    return a

sum = int(input('Сумма вклада: '))
date = int(input('Сроком на: '))

print(bank(sum, date))

# задача 6 Простые числа
"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
"""

# задача 7 Правильная дата
"""
Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""