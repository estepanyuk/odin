# задача 1 Простейшие арифметические операции
"""

"""
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
        return "Неизвестная операция"

a1 = int(input("Первое значение: "))
a2 = int(input("Второе значение: "))
o = input("Операция(+,-,*,/): ")

print(arithmetic(a1, a2, o))

#задача 2 Високосный год
"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""
def is_year_leap(year):
    if year % 4 == 0:
        return True
    return False

year = int(input('Какой сейчас год? '))
print(is_year_leap(year))

#вариант 2
data = int(input('Какой сейчас год? '))
x = data % 4

def leapYear(x):

    if x > 0:
        print('Год невисокосный')
    else:
        print('Год високосный')

leapYear(x)

# задача 3 Времена года
"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
"""
def season(num):
	if num in (12, 1, 2):
		return "зима"
	elif num in (3, 4, 5):
		return "весна"
	elif num in (6, 7, 8):
		return "лето"
	elif num in (9, 10, 11):
		return "осень"
	else:
		return "неправильный номер месяца"

month = int(input("введите номер месяца: "))
print(season(month))

#задача 4 Квадрат
"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения 
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""
from math import sqrt

def square(a):
    perimeter = a * 4
    area = a ** 2
    diagonal = round(a * sqrt(2), 2)  # d = x√2

    return perimeter, area, diagonal

while True:
    c = square(int(input('Сторона a = ')))
    print(c[0], " - Периметр", "\n", c[1], " - Площадь", "\n", c[2], " - Диагональ", sep="")


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

sum = int(input("Сумма вклад: "))
date = int(input("Сроком на : "))
print(bank(sum, date))

# задача 6 Простые числа
"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
"""
def is_prime(x):
	result = (x == 2 or x % 2 != 0)

	if result:
		for i in range(3, int(x**0.5), 2):
			if x % i == 0:
				return False

	return result

print(is_prime(2))

#вариант 2
from cmath import sqrt

def is_prime(number):
    # Все четные числа кроме 2 непростые
    if number % 2 == 0 and number != 2:
        return False
    # 0 и 1 не являются простыми
    if number == 0 or number == 1:
        return False
    # Перебираем числа от 3 до корня из введенного, шаг - 2
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  # Если число делится нацело, то оно непростое
            return False
    return True  # Остальные числа простые

n = int(input('Введите число: '))
print(is_prime(n))

# задача 7 Правильная дата
"""
Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""
def is_year_leap(year):
    if year % 4 == 0:
        return True
    return False

def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

print("{0}.{1}.{2}: {3}".format(day, month, year, date(day, month, year)))

#вариант 2
def date_cheat(day, month, year):
    """Проще, но это непедагогично :)"""
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True
