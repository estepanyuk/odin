#задача 1
#вариант 1
a1 = int(input())
a2 = int(input())
a3 = int(input())
if a3-a2 == a2-a1:
    print("Да, являются")
else:
    print("Нет, не являются")

#вариант 2
# Ввод трех чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Проверка на арифметическую прогрессию
if b - a == c - b:
    print("Да, являются арифметической прогрессией.")
else:
    print("Нет, не являются арифметической прогрессией.")

#Задача 2
#вариант 1
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('Год високосный')
else:
    print('Не високосный год')

#вариант 2
year = int(input('Введите год: '))
if year % 4 != 0:
    print('Год не високосный.')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')
else:
    print('Год високосный.')

#Задача 3
#вариант 1
old = int(input('Ваш возраст: '))

print('Рекомендовано:', end=' ')

if 3 <= old < 6:
    print('"Синий трактор"')
elif 6 <= old < 12:
    print('"Звездые войны"')
elif 12 <= old < 16:
    print('"Человек паук"')
elif 16 <= old:
    print('"Первому игроку приготовится"')


#вариант 2
a = int(input('Введите ваш возраст: '))
print('Ваш возраст = ', a)
if a <= 2:
    print('Рекомендован фильм: Чебурашка')
elif 2 < a < 7:
    print('Рекомендован фильм: Человек Паук')
elif 6 < a < 13:
    print('Рекомендован фильм: Барби')
elif 13 < a < 17:
    print('Рекомендован фильм: Оппенгеймер')
elif a > 16:
    print('Рекомендован фильм: Бойцовский клуб')


